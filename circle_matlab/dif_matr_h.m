function [h] = dif_matr_h(n1_fin,n2_fin,n3_fin, num_val);
h=[];
for k=1:num_val
    h(1,k)=n1_fin(k)*n1_fin(k);
    h(2,k)=n2_fin(k)*n2_fin(k);
    h(3,k)=n3_fin(k)*n3_fin(k);
    h(4,k)=n1_fin(k)*n2_fin(k);
    h(5,k)=n1_fin(k)*n3_fin(k);
    h(6,k)=n2_fin(k)*n3_fin(k);
    h(7,k)=n1_fin(k);
    h(8,k)=n2_fin(k);
    h(9,k)=n3_fin(k);
end
end

