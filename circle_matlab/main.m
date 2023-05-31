clc; clear all;

N=8; num_layers=N/4+1; theta_star= 54.7356;
%lenth=(2*pi)/N; old_deg=lenth*180/pi; 
% сетка значений углов по широте k (слои)

for n=1:num_layers
    k_j(n) = (n-1.)*(2*pi/N);
    %rad(n) =cos(k_j(n));
end


% для каждого слоя k сетка значений phi 
%end_j конечное значение step шаги для слоев j_num матрица значений i по j
for j=1:num_layers
    num_axes(j,:)=floor(N*cos(k_j(j))+1);
end
num_axes(num_layers)=1;

for j=1:num_layers
    for i=1:num_axes(j)
        phi_ij(j,i)=((i-1)*2*pi)/(N*cos(k_j(j))+1);
    end
end



%переход от сферических к декартовым координатам
for j=1:num_layers
    for i=1:num_axes(j)
        n1(j, i)=sin(k_j(j));
    end
end
for j=1:num_layers
    for i=1:num_axes(j)
        n2(j, i)=cos(phi_ij(j,i))*cos(k_j(j));
    end
end
for j=1:num_layers
    for i=1:num_axes(j)
        n3(j, i)=sin(phi_ij(j,i))*cos(k_j(j)) ;
    end
end

%перенумеровка массивов и их "вытягивание"
n_all=[];n1_fin=[];n2_fin=[];n3_fin=[];
for j=1:num_layers
    for i=1:num_axes(j)
        n_all(end+1)=n1(j,i);
        n1_fin(end+1)=n1(j,i);
    end
end
for j=2:num_layers
    for i=1:num_axes(j)
        n_all(end+1)=-n1(j,i);
        n1_fin(end+1)=-n1(j,i);
    end
end
for j=1:num_layers
    for i=1:num_axes(j)
        n_all(end+1)=n2(j,i);
        n2_fin(end+1)=n2(j,i);
    end
end
for j=2:num_layers
    for i=1:num_axes(j)
        n_all(end+1)=-n2(j,i);
        n2_fin(end+1)=-n2(j,i);
    end
end
for j=1:num_layers
    for i=1:num_axes(j)
        n_all(end+1)=n3(j,i);
        n3_fin(end+1)=n3(j,i);
    end
end
for j=2:num_layers
    for i=1:num_axes(j)
        n_all(end+1)=-n3(j,i);
        n3_fin(end+1)=-n3(j,i);
    end
end

num_val=sum(num_axes)+sum(num_axes)-num_axes(1);
H=big_matr_h(n1_fin, n2_fin, n3_fin, num_val);

c=[];
for k=1:num_val
    c(end+1) =1/3*(abs((n1_fin(k)/cos(theta_star)) - (2* n2_fin(k)/sin(theta_star))) + abs((n1_fin(k)/cos(theta_star)) +(n2_fin(k) + sqrt(3) * n3_fin(k))/sin(theta_star)) + abs((n1_fin(k)/cos(theta_star)) +(n2_fin(k) - sqrt(3) * n3_fin(k))/sin(theta_star)));
end



Hnew = dif_matr_h(n1_fin, n2_fin, n3_fin, num_val);
a = [cos(theta_star)*cos(theta_star),sin(theta_star)*sin(theta_star),0,-sin(theta_star)*cos(theta_star),0,0,0,0,0];
deltC=[c,c];
deltH=[Hnew, -Hnew];
zero =zeros(size(deltC));
x =linprog(deltC,[],[],deltH,a,zero);


deltHTrans =deltH';

x_d=linprog(-a,deltHTrans,deltC,[],[],a);


