import numpy as np
Map_collision = np.array([[0,0,1,0,0,0],
                          [0,0,0,0,0,0],
                          [0,0,1,0,0,0],
                          [0,0,0,0,0,0],])
player_pos = (2,0)
player_final = (2,3)

def coef_direct_deux_points(pos1,pos2):
    a = (pos2[1] -pos1[1])/(pos2[0]-pos1[0])
    return a, pos1[1] - a * pos1[0]
A,B = coef_direct_deux_points(player_pos,player_final)
print(coef_direct_deux_points(player_pos,player_final))

def collide_point(x_debut,x_max,y_debut,y_max,a,b):
    Liste_points = []
    for x in range(int(x_debut),int(x_max)+1):
        Liste_points.append((x,a*x+b))
        y = a*x + b

        print(Map_collision[int(y),x])
        # print(x,int(y))
    for y in range(int(y_debut)+1,int(y_max)+1):
        Liste_points.append(((y-b)*(a**-1),y))
    return Liste_points

L_points = collide_point(player_pos[0],player_final[0],player_pos[1],player_final[1],A,B)
print(L_points)


# x = 3.001
# if int(x)==x:
#     print(True)