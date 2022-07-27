N = 4;
neff = 1.447;

Time = 0:0.001:5;
Temp_polynomials = [getPolynomial;getPolynomial;getPolynomial;getPolynomial([0 5],[25 600])];

Temps = zeros(N,length(Time));
for i=1:N
    Temps(i,:) = polyval(Temp_polynomials(i,:),Time);
end

Periods = [533,531.6,532.6,533]; %nm
Lengths = [3,3,3,3]; %mm
Deltaneffs = [3,3,3,3,3]*1e-3; %[a.u.]

tuning_range = 9.6133; %nm
lambda_tuning_start = 1541.2327; %nm

% Temp_inits = [25,300,250]; %Celsius
% Temp_ranges = [300,600,400]; %Celsius


Thermooptic_polynomials = [0,0.011,0;...
    0,0.011,0;...
    0,0.011,0;...
    0,0.011,0]; %[a1,b1,c1;a2,b2,c2;...]     a*T^2+b*T+c

%%%
braggs_no_temp = Periods(1:N)*2*neff;
braggs_w_temp = zeros(N,length(Time));
for i=1:N
    braggs_w_temp(i,:) = braggs_no_temp(i) + polyval(Thermooptic_polynomials(i,:),Temps(i,:));
end

%%%
LW = 3;
leg_ = {};
figure('color','w');
subplot(1,2,1)
plot(Time,Temps,'--','LineWidth',LW)
legend(leg_,'Location','best')

subplot(1,2,2)
for i=1:N
    plot(Temps(i,:),braggs_w_temp(i,:),'--','LineWidth',LW);
    hold on;
    leg_{i} = ['Siatka ' num2str(i)];
end
plot([min(Temps(:)) max(Temps(:))], [lambda_tuning_start, lambda_tuning_start], 'Color','r')
plot([min(Temps(:)) max(Temps(:))], [lambda_tuning_start,lambda_tuning_start]+tuning_range, 'Color','r')
legend(leg_,'Location','best')
xlabel('Temperatura [^oC]')
ylabel('Dł. fali [nm]')


%%% wyswietlanie
disp(['Number of gratings [#]: ' num2str(N)])
disp(['Periods [nm]: ' num2str(Periods)])
disp(['Lengths [mm]: ' num2str(Lengths)])
disp(['Bragg_init [nm]: ' num2str(2*Periods*neff)])
disp(['Deltaneffs [a.u.]: ' num2str(Deltaneffs)])
disp(['T_init [oC]: ' num2str(Temp_inits)])
disp(['T_range [oC]: ' num2str(Temp_ranges)])
for i=1:N
disp(['Polynomial for ' num2str(i) 'grating: ' num2str(Thermooptic_polynomials(i,:))])
end