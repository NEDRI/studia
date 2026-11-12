function buduj_zad3_zad4()
%BUDUJ_ZAD3_ZAD4  Dobudowuje zadania 3 i 4 do modelu z zadaniami 1-2.
%
%   Wejście:  ~/Downloads/DoZrobienia3i4.slx   (zadania 1-2, zapis R2025a)
%   Wyjście:  Bramki_zad1_4.slx                (format R2025a, otwiera się w sali)
%             schematy/*.png                   (schematy do sprawozdania)
%
%   Każdy podpunkt jest osobnym podsystemem (Zad3a ... Zad4f). W środku są dwa
%   układy na tych samych wejściach i bramka XOR, która porównuje ich wyjścia.
%   XOR = 0 dla każdej kombinacji wejść oznacza, że układy są równoważne.
%   Wejścia A, B, C, D (Constant + Toggle Switch) są wspólne dla zadań 3 i 4
%   i trafiają do podsystemów przez bloki Goto/From.
%   Opis układów jest w zadania_def.m.

here   = fileparts(mfilename('fullpath'));
src    = fullfile(getenv('HOME'),'Downloads','DoZrobienia3i4.slx');
final  = fullfile(here,'Bramki_zad1_4.slx');
pngDir = fullfile(here,'schematy');
work   = fullfile(tempdir,'bramki_build');

if exist(work,'dir'), rmdir(work,'s'); end
mkdir(work);
if ~exist(pngDir,'dir'), mkdir(pngDir); end
Simulink.fileGenControl('set','CacheFolder',work,'CodeGenFolder',work);
load_system('simulink');

% Kopia modelu z zadaniami 1-2 (oryginał w Downloads zostaje nietknięty)
copyfile(src, fullfile(work,'DoZrobienia3i4.slx'));
load_system(fullfile(work,'DoZrobienia3i4.slx'));
mdl = 'Bramki_zad1_4_build';
save_system('DoZrobienia3i4', fullfile(work,[mdl '.slx']));

% Usuń niepodłączone zaślepki Constant6..Constant11 (początek zad. 3/4)
for k = 6:11
    b = sprintf('%s/Constant%d', mdl, k);
    if getSimulinkBlockHandle(b) > 0 && ~maPolaczenia(b)
        delete_block(b);
    end
end

% Nowe elementy stawiamy pod istniejącymi zadaniami 1-2
blks = find_system(mdl,'SearchDepth',1,'Type','Block');
pos  = cell2mat(get_param(blks,'Position'));
X0 = min(pos(:,1));
Y0 = max(pos(:,4)) + 140;

%% Wspólne wejścia A, B, C, D
vars = {'A','B','C','D'};
for i = 1:4
    x = X0 + 20 + (i-1)*260;
    tog = sprintf('%s/Przelacznik %s', mdl, vars{i});
    c   = [mdl '/' vars{i}];
    g   = [mdl '/Goto ' vars{i}];
    add_block([mdl '/Toggle Switch'], tog, ...   % kopia przełącznika z zad. 1
              'Position',[x Y0+50 x+55 Y0+150], 'ShowName','off');
    add_block('simulink/Sources/Constant', c, 'Value','0', 'SampleTime','0.1', ...
              'OutDataTypeStr','boolean', ...      % jak w pkt 3.1.4 instrukcji
              'Position',[x+95 Y0+85 x+125 Y0+115]);
    add_block('simulink/Signal Routing/Goto', g, 'GotoTag',vars{i}, ...
              'Position',[x+165 Y0+88 x+215 Y0+112], 'ShowName','off');
    polacz(mdl, c, 1, g, 1);
    bind = Simulink.HMI.ParamSourceInfo;
    bind.BlockPath = Simulink.BlockPath(c);
    bind.ParamName = 'Value';
    set_param(tog, 'Binding', bind);
    set_param(tog, 'States', struct('Value',{0,1}, 'Label',{'0','1'}));
end
notatka(mdl, ['Wejścia A, B, C, D – wspólne dla zadań 3 i 4. ' ...
              'Przełącznik ustawia wartość bloku Constant (0 lub 1).'], ...
        [X0 Y0 X0+1060 Y0+185], true);

%% Zadania 3 i 4: wiersz = podsystem + Mux + Display
Z = zadania_def();
Y3   = Y0 + 300;
X4   = X0 + 1300;
kol  = struct('x',{X0, X4}, 'y',{Y3, Y3});
tytul = {['Zadanie 3 – upraszczanie wyrażeń.  Display: [F; F_upr; XOR],  ' ...
          'XOR = 0 → układy równoważne'], ...
         ['Zadanie 4 – bramki z podanych elementów.  Display: [Y; Y_wz; XOR],  ' ...
          'XOR = 0 → zgodne z wzorcem']};
ramka = [inf inf -inf -inf; inf inf -inf -inf];

for z = Z
    j = z.id(1) - '2';              % '3' -> kolumna 1, '4' -> kolumna 2
    [h, box] = wierszTopLevel(mdl, z, kol(j).x + 40, kol(j).y + 50);
    kol(j).y = kol(j).y + h;
    ramka(j,:) = [min(ramka(j,1),box(1)) min(ramka(j,2),box(2)) ...
                  max(ramka(j,3),box(3)) max(ramka(j,4),box(4))];
    budujPodsystem([mdl '/Zad' z.id], z);
end
for j = 1:2
    r = ramka(j,:);
    notatka(mdl, tytul{j}, [r(1)-40 r(2)-60 max(r(3)+40, r(1)+1180) r(4)+30], true);
end

%% Zapis, eksport do R2025a i schematy PNG
save_system(mdl);
eksportPng(mdl, fullfile(pngDir,'model_caly.png'));
for z = Z
    eksportPng([mdl '/Zad' z.id], fullfile(pngDir, ['zad' z.id '.png']));
end
if exist(final,'file'), delete(final); end
Simulink.exportToVersion(mdl, final, 'R2025a');
close_system(mdl, 0);
fprintf('Zapisano %s (R2025a) i schematy w %s\n', final, pngDir);
end

%% ======================= funkcje pomocnicze =======================

function [h, box] = wierszTopLevel(mdl, z, x, y)
% From -> podsystem -> Mux -> Display, obok opis wzoru. Zwraca wysokość wiersza.
n  = numel(z.vars);
H  = 30*max(n,3);
sub = [mdl '/Zad' z.id];
add_block('built-in/Subsystem', sub, 'Position',[x+110 y x+250 y+H]);
for i = 1:n                                   % porty muszą istnieć przed liniami
    add_block('built-in/Inport',  [sub '/' z.vars{i}], 'Port',num2str(i));
end
for i = 1:3
    add_block('built-in/Outport', [sub '/' z.outNames{i}], 'Port',num2str(i));
end
for i = 1:n
    py = y + H*(2*i-1)/(2*n);
    f = sprintf('%s/From %s %s', mdl, z.vars{i}, z.id);
    add_block('simulink/Signal Routing/From', f, 'GotoTag',z.vars{i}, ...
              'Position',[x py-10 x+50 py+10], 'ShowName','off');
    polacz(mdl, f, 1, sub, i);
end
mux  = [mdl '/Mux ' z.id];
disp_ = sprintf('%s/%s: [%s]', mdl, z.id, strjoin(z.outNames,'; '));
add_block('simulink/Signal Routing/Mux', mux, 'Inputs','3', 'ShowName','off', ...
          'Position',[x+320 y x+325 y+H]);
add_block('simulink/Sinks/Display', disp_, ...
          'Position',[x+380 y+H/2-32 x+480 y+H/2+32]);
ph = get_param(sub,'PortHandles');
for i = 1:3
    polacz(mdl, sub, i, mux, i);
    set_param(ph.Outport(i), 'DataLogging','on', 'DataLoggingNameMode','Custom', ...
              'DataLoggingName', sprintf('z%s_%s', z.id, z.outNames{i}));
end
polacz(mdl, mux, 1, disp_, 1);
notatka(mdl, z.opis, [x+520 y+H/2-12 x+1120 y+H/2+12], false);
h   = H + 55;
box = [x y x+1120 y+H+20];
end

function budujPodsystem(sub, z)
% Rysuje wnętrze podsystemu: wejścia, oba układy, porównanie XOR i wyjścia.
W = 40;  x0 = 150;  rel = 15 + 55*(0:numel(z.vars)-1);
inY = containers.Map(z.vars, num2cell(rel));
top1 = 70;
for i = 1:numel(z.vars)
    set_param([sub '/' z.vars{i}], 'Position',[30 top1+rel(i)-7 60 top1+rel(i)+7]);
end
[o1, y1, b1] = pasmo(sub, z.gates1, z.out1, inY, top1, x0);
top2 = b1(4) + 100;
[o2, y2, b2] = pasmo(sub, z.gates2, z.out2, inY, top2, x0);
if isempty(z.gates2), y2 = top2 + 15; b2 = [x0-35 top2-40 x0+200 top2+30]; end

% Ramki z opisem układów (szerokość dopasowana do tytułu)
b1(3) = max(b1(3), b1(1) + 7.5*numel(z.title1));
b2(3) = max(b2(3), b2(1) + 7.5*numel(z.title2));
notatka(sub, z.title1, b1, true);
if isempty(z.gates2)
    notatka(sub, z.title2, [b2(1) b2(2) b2(1)+7.5*numel(z.title2) b2(2)+20], false);
else
    notatka(sub, z.title2, b2, true);
end

% Porównanie wyjść bramką XOR
xc = max(b1(3), b2(3)) + 80;   yc = (y1 + y2)/2;
cmp = [sub '/porównanie'];
add_block('simulink/Logic and Bit Operations/Logical Operator', cmp, ...
          'Operator','XOR', 'Inputs','2', 'IconShape','distinctive', ...
          'AllPortsSameDT','off', 'OutDataTypeStr','boolean', ...
          'Position',[xc yc-20 xc+W yc+20]);
tk = 'Kontrola: XOR = 0 ⇒ układy zgodne';
bc = [xc-30 yc-65 max(xc+W+30, xc-30+7.5*numel(tk)) yc+45];
notatka(sub, tk, bc, true);
polaczH(sub, o1, cmp, 1);
polaczH(sub, o2, cmp, 2);

% Wyjścia podsystemu
xo = bc(3) + 50;
ys = [y1 y2 yc];
src = {o1, o2, get_param(cmp,'Handle')};
for i = 1:3
    op = [sub '/' z.outNames{i}];
    set_param(op, 'Position',[xo ys(i)-7 xo+30 ys(i)+7]);
    polaczH(sub, src{i}, op, 1);
end
end

function [outH, outY, box] = pasmo(sys, gates, outId, inY, top, x0)
% Rozmieszcza bramki jednego układu warstwami (głębokość w grafie) i łączy je.
% Zwraca uchwyt bloku wyjściowego, jego środek w pionie i ramkę układu.
W = 40;  dx = 150;  gap = 38;
n = size(gates,1);
ids = gates(:,1);
nin = cellfun(@numel, gates(:,3));
hgt = max(30, 12*nin + 16);
% Kolumny: negacje wejść (¬A, ¬B, ...) tworzą pierwszą kolumnę razem
% z wejściami, a każda kolejna bramka stoi o kolumnę za swoim
% najpóźniejszym źródłem.
negWej = strcmp(gates(:,2),'NOT') & cellfun(@(c) ~any(ismember(c, ids)), gates(:,3));
glWej  = double(any(negWej));                 % "głębokość" samych wejść
depth = zeros(n,1);  yc = zeros(n,1);
for i = 1:n                                   % lista jest uporządkowana topologicznie
    if negWej(i), depth(i) = 1; continue; end
    d = glWej;
    for s = gates{i,3}
        k = find(strcmp(ids, s{1}));
        if ~isempty(k), d = max(d, depth(k)); end
    end
    depth(i) = d + 1;
end
for d = 1:max([depth; 0])
    idx = find(depth == d)';
    want = zeros(size(idx));
    for t = 1:numel(idx)
        ys = cellfun(@(s) srcY(s), gates{idx(t),3});
        want(t) = mean(ys);
    end
    if d == 1
        % pierwsza kolumna: każda bramka jak najbliżej swoich wejść
        [want, o] = sort(want);  idx = idx(o);
        prevBottom = top - gap;
        for t = 1:numel(idx)
            i = idx(t);
            yc(i) = max(want(t), prevBottom + gap + hgt(i)/2);
            prevBottom = yc(i) + hgt(i)/2;
        end
    else
        % dalsze kolumny: kolejność jak we wzorze, wyśrodkowane na źródłach
        total = sum(hgt(idx)) + gap*(numel(idx)-1);
        yTop = max(top, mean(want) - total/2);
        for t = 1:numel(idx)
            i = idx(t);
            yc(i) = yTop + hgt(i)/2;
            yTop = yTop + hgt(i) + gap;
        end
    end
end
H = zeros(n,1);
for i = 1:n
    x = x0 + (depth(i)-1)*dx;
    p = [sys '/' gates{i,4}];
    if getSimulinkBlockHandle(p) > 0, error('Powtórzona nazwa bloku: %s', p); end
    H(i) = add_block('simulink/Logic and Bit Operations/Logical Operator', p, ...
        'Operator',gates{i,2}, 'Inputs',num2str(nin(i)), 'IconShape','distinctive', ...
        'AllPortsSameDT','off', 'OutDataTypeStr','boolean', ...
        'Position',[x yc(i)-hgt(i)/2 x+W yc(i)+hgt(i)/2]);
end
for i = 1:n
    for k = 1:nin(i)
        polaczH(sys, srcH(gates{i,3}{k}), H(i), k);
    end
end
outH = srcH(outId);  outY = srcY(outId);
if n == 0
    box = [x0-35 top-40 x0+60 top+30];
else
    xs = x0 + (depth-1)*dx;
    box = [x0-35 top-45 max(xs)+W+60 max(yc+hgt/2)+30];
end

    % (zmienne lokalne o innych nazwach niż w funkcji nadrzędnej,
    %  bo funkcje zagnieżdżone współdzielą z nią przestrzeń zmiennych)
    function yOut = srcY(nazwa)
        kz = find(strcmp(ids, nazwa));
        if isempty(kz), yOut = top + inY(nazwa); else, yOut = yc(kz); end
    end
    function hOut = srcH(nazwa)
        kz = find(strcmp(ids, nazwa));
        if isempty(kz), hOut = get_param([sys '/' nazwa],'Handle'); else, hOut = H(kz); end
    end
end

function polacz(sys, a, pa, b, pb)
ha = get_param(a,'PortHandles');  hb = get_param(b,'PortHandles');
add_line(sys, ha.Outport(pa), hb.Inport(pb), 'autorouting','smart');
end

function polaczH(sys, a, b, pb)
% a: uchwyt bloku źródłowego (wyjście 1), b: ścieżka lub uchwyt bloku docelowego
ha = get_param(a,'PortHandles');  hb = get_param(b,'PortHandles');
add_line(sys, ha.Outport(1), hb.Inport(pb), 'autorouting','smart');
end

function tf = maPolaczenia(b)
pc = get_param(b,'PortConnectivity');
tf = false;
for p = pc'
    if any(p.SrcBlock > 0) || any(p.DstBlock > 0), tf = true; end
end
end

function notatka(sys, txt, pos, obszar)
% Adnotacja tekstowa albo obszar (Area) z tytułem.
pos = round(pos);
if obszar
    try
        add_block('built-in/Area', [sys '/' strrep(txt,'/','//')], 'Position', pos);
        return
    catch e
        warning('Area przez add_block nie działa (%s), wstawiam notatkę.', e.message);
    end
end
a = Simulink.Annotation([sys '/notatka_tmp']);
a.Text = txt;
a.HorizontalAlignment = 'left';
if obszar
    a.Position = pos;                       % ramka w miejscu obszaru
else
    a.Position = pos;
end
end

function eksportPng(sys, plik)
try
    print(['-s' sys], '-dpng', plik);
catch e
    warning('Nie udało się wyeksportować %s: %s', sys, e.message);
end
end
