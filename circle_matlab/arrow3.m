function arrow3(X1, X2, r1, h ,r2, color)
hold on;
cylinder3(X1,X2, r1,color);
X3=(X2-X1)/norm(X2-X1)*h+X2;
cone3(X2,X3,r2,color);
end


