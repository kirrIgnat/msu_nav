clc; clear all;
N=80; num_layers=N/4+1; lenth=(2*pi)/N; old_deg=lenth*180/pi;

% сетка значений углов по k (слои)
%end_j конечное значение step шаги для слоев j_num вектор значений j
%end_j=N/4+1;step_j=(end_j-1)/(num_layers-1); j_num=1.0:step_j:end_j;
for n=1:num_layers
    k_j(n) = (n-1.)*(2*pi/N);
    rad(n) =cos(k_j(n));
end

% для каждого слоя k сетка значений phi 
%end_j конечное значение step шаги для слоев j_num матрица значений i по j
for j=1:num_layers

    num_axes(j,:)=N*cos(k_j(j))+2;
end
num_axes(num_layers)=1;
for j=1:num_layers
    for i=1:num_axes(j)
        phi_ij(j,i)=((i-1)*2*pi)/(N*cos(k_j(j))+1);
    end
end



for j=1:num_layers
    for i=1:num_axes(j)
        n1(j, i)=cos(phi_ij(j,i))*cos(k_j(j));
    end
end
for j=1:num_layers
    for i=1:num_axes(j)
        n2(j, i)=sin(phi_ij(j,i))*cos(k_j(j));
    end
end
for j=1:num_layers
    for i=1:num_axes(1)
        n3(j, i)=sin(k_j(j));
    end
end


n1_fin=[n1.';-n1.'];
n2_fin=[n2.';-n2.'];
n3_fin=[n3.';-n3.'];

n1_fin (N+2, :) =[];
n2_fin (N+2, :) =[];
n3_fin (N+2, :) =[];

nn1 = n1.';
nn2 = n2.';
nn3 = n3.';
nnm1 = -n1.';
nnm2 = -n2.';
nnm3 = -n3.';
%n_all=[n1_fin;n2_fin;n3_fin];
figure;
%surf(nn1,nn2,nn3);
 surf(nn1,nn2,nn3,...
     'AlignVertexCenters','on',...
    'LineWidth',0.2,...
    'FaceAlpha',0.2,...
    'FaceColor',[0.07 0.6 1],...
    'EdgeAlpha',0.2)
 hold on
 %surf(nnm1,nnm2,nnm3);
 surf(nnm1,nnm2,nnm3,...
     'AlignVertexCenters','on',...
    'LineWidth',0.2,...
    'FaceAlpha',0.2,...
    'FaceColor',[0.07 0.6 1],...
    'EdgeAlpha',0.2)




text(-1.5,0,0, 'z','Color','red','FontSize',20)
text(0,1.57,0, 'y','Color','red','FontSize',20)
text(0,0,1.55, 'x','Color','red','FontSize',20)

arrow3([0 0 0],[-1.4 0 0],0.02,0.1,0.04,'r')
arrow3([0 0 0],[0 1.4 0],0.02,0.1,0.04,'r')
arrow3([0 0 0],[0 0 1.4],0.02,0.1,0.04,'r')
axis off;


%set(gca,'xtick',[])
%set(gca,'ytick',[])
%set(gca,'ztick',[])
