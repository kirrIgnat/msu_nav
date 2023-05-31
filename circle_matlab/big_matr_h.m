function [h] = big_matr_h(n1_fin,n2_fin,n3_fin, num_val);
h=[];
for k=1:num_val
    h(end+1)=n1_fin(k)*n1_fin(k);
end
for k=1:num_val
    h(end+1)=n2_fin(k)*n2_fin(k);
end
for k=1:num_val
    h(end+1)=n3_fin(k)*n3_fin(k);
end
for k=1:num_val
    h(end+1)=n1_fin(k)*n2_fin(k);
end
for k=1:num_val
    h(end+1)=n1_fin(k)*n3_fin(k);
end
for k=1:num_val
    h(end+1)=n2_fin(k)*n3_fin(k);
end
for k=1:num_val
    h(end+1)=n1_fin(k);
end
for k=1:num_val
    h(end+1)=n2_fin(k);
end
for k=1:num_val
    h(end+1)=n3_fin(k);
end