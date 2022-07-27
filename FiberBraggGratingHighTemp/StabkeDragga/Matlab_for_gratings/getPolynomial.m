function [P] = getPolynomial(time,temp)
if nargin<2


    time = [0 0.1 1 2 3 5]; %in seconds
    temp = [40 100 200 300 300 300]; %Celsius degrees


end

P = polyfit(time,temp,2);

%figure;plot(time,temp);hold on;plot(spline(1:length(time),time,1:0.001:length(time)),polyval(P,spline(1:length(time),time,1:0.001:length(time))))
end

