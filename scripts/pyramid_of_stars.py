'''Print a downward half-pyramid pattern of stars'''

def downward_pyramid_of_stars(n):
    for i in range(n,0,-1):
        print(" * " * i)
    for i in range(0,n+1,1):
        print(" * " * i)

downward_pyramid_of_stars(5)