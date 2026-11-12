function weryfikuj_zad3_zad4()
%WERYFIKUJ_ZAD3_ZAD4  Symuluje Bramki_zad1_4.slx dla wszystkich 16 kombinacji
%   wejść A, B, C, D i sprawdza zadania 3 i 4:
%     - XOR porównujący oba układy musi być 0 w każdym wierszu,
%     - wyniki symulacji muszą się zgadzać z funkcjami z zadania_def.m.
%   Tabele prawdy z symulacji zapisuje do wyniki_symulacji.md.
%   Model nie jest zapisywany, więc plik .slx zostaje bez zmian.

here = fileparts(mfilename('fullpath'));
plik = fullfile(here,'Bramki_zad1_4.slx');
work = fullfile(tempdir,'bramki_verify');
if ~exist(work,'dir'), mkdir(work); end
Simulink.fileGenControl('set','CacheFolder',work,'CodeGenFolder',work);

load_system(plik);
mdl = 'Bramki_zad1_4';

% Powiązania przełączników z blokami Constant (kontrola po eksporcie)
tog = find_system(mdl,'SearchDepth',1,'BlockType','ToggleSwitchBlock');
for i = 1:numel(tog)
    b = get_param(tog{i},'Binding');
    fprintf('%-32s -> %s . %s\n', strrep(tog{i},newline,' '), ...
            b.BlockPath.getBlock(1), b.ParamName);
end

% 16 symulacji: wiersz k = kombinacja (A B C D), A to najstarszy bit
vars = {'A','B','C','D'};
K = dec2bin(0:15) - '0';
in = Simulink.SimulationInput.empty;
for k = 1:16
    s = Simulink.SimulationInput(mdl);
    s = s.setModelParameter('StopTime','0.2');
    for v = 1:4
        s = s.setBlockParameter([mdl '/' vars{v}], 'Value', num2str(K(k,v)));
    end
    in(k) = s;
end
out = sim(in, 'ShowProgress','off', 'UseFastRestart','on');

Z = zadania_def();
fid = fopen(fullfile(here,'wyniki_symulacji.md'),'w','n','UTF-8');
fprintf(fid,'# Wyniki symulacji – zadania 3 i 4\n\n');
fprintf(fid,['Model `Bramki_zad1_4.slx`, %d symulacji (wszystkie kombinacje A, B, C, D). ' ...
             'Wartości odczytane z zalogowanych wyjść podsystemów. ' ...
             'Tabela pokazuje tylko zmienne, z których korzysta dany podpunkt.\n\n'], numel(in));
wszystkoOk = true;
for z = Z
    n = numel(z.vars);
    val = zeros(16,3);
    for k = 1:16
        for i = 1:3
            el = out(k).logsout.getElement(sprintf('z%s_%s', z.id, z.outNames{i}));
            val(k,i) = double(el.Values.Data(end));
        end
    end
    a = num2cell(logical(K),1);
    exp1 = double(z.f1(a{:}));  exp2 = double(z.f2(a{:}));
    ok = all(val(:,3) == 0) && isequal(val(:,1), exp1) && isequal(val(:,2), exp2);
    wszystkoOk = wszystkoOk && ok;
    fprintf('%s: %s\n', z.id, tern(ok,'OK – XOR = 0 we wszystkich 16 kombinacjach','BŁĄD'));

    fprintf(fid,'## %s\n\n', z.opis);
    fprintf(fid,'| %s | %s |\n', strjoin(z.vars,' | '), strjoin(z.outNames,' | '));
    fprintf(fid,'|%s\n', repmat('---|',1,n+3));
    rows = find(all(K(:,n+1:end) == 0, 2))';    % zmienne nieużywane = 0
    for k = rows
        fprintf(fid,'| %s | %s |\n', strjoin(string(K(k,1:n)),' | '), ...
                strjoin(string(val(k,:)),' | '));
    end
    fprintf(fid,'\nWynik kontroli: **%s**\n\n', ...
            tern(ok, sprintf('XOR = 0 dla wszystkich %d kombinacji, układy zgodne', 2^n), ...
                     'NIEZGODNOŚĆ'));
end
fclose(fid);
close_system(mdl, 0);
if wszystkoOk
    fprintf('WSZYSTKO OK\n');
else
    error('Wykryto niezgodność – sprawdź wyniki_symulacji.md');
end
end

function s = tern(c, a, b)
if c, s = a; else, s = b; end
end
