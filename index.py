# Part I

def draw_stars(x):
    for i in range(len(x)):
        
        for j in range(x[i]):
            print "*",
        print "\n"


        
x = [4, 6, 1, 3, 5, 7, 25]
draw_stars(x)


# Part II

def draw_starAlpha(x):
    for i in range(len(x)):

            if isinstance(x[i], int):
                for j in range(x[i]):
                    print "*",
            elif isinstance(x[i], str):
                for j in range(len(x[i])):
                    print x[i][0].lower(),
            print "\n"



x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_starAlpha(x)