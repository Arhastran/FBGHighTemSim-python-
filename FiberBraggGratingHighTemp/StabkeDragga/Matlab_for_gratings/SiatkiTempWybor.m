C = 0.019; %nm/oC

W_L = 1541.2327;
W_R = 1550.8460;

lmb_brgs = [1526,1530,1534,1536,1544,1548,1550];

tmp_start = 25 + (W_L-lmb_brgs)./C;
tmp_end = 25 + (W_R-lmb_brgs)./C;

disp([['T_init: ';'T_end:  '],num2str([tmp_start;tmp_end])])