function cone3(X1, X2, r, color)
length_cyl=norm(X2-X1);
[x,y,z]=cylinder(linspace(r,0,50),100);
z=z*length_cyl;

hold on;
EndPlate1=fill3(x(1,:),y(1,:),z(1,:),'r');
Cylinder=mesh(x,y,z);

unit_V=[0 0 1];
angle_X1X2=acos(dot(unit_V,(X2-X1) )/( norm(unit_V)*norm(X2-X1)) )*180/pi;

axis_rot=cross(unit_V,(X2-X1));

if angle_X1X2~=0 
    rotate(Cylinder,axis_rot,angle_X1X2,[0 0 0])
    rotate(EndPlate1,axis_rot,angle_X1X2,[0 0 0])
end

set(EndPlate1,'XData',get(EndPlate1,'XData')+X1(1))
set(EndPlate1,'YData',get(EndPlate1,'YData')+X1(2))
set(EndPlate1,'ZData',get(EndPlate1,'ZData')+X1(3))
set(Cylinder,'XData',get(Cylinder,'XData')+X1(1))
set(Cylinder,'YData',get(Cylinder,'YData')+X1(2))
set(Cylinder,'ZData',get(Cylinder,'ZData')+X1(3))

set(Cylinder,'FaceColor',color)
set(EndPlate1,'FaceColor',color)
set(Cylinder,'EdgeAlpha',0)
set(EndPlate1,'EdgeAlpha',0)
axis equal;
view(3)
end

