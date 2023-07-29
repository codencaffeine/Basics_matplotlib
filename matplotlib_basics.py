import numpy as np
import matplotlib.pyplot as plt

#! Uncomment the plt.show() to view each plots

if __name__ == "__main__":
    
    #Example of creating a simple pie chart
    #==============================================================================================================
    animals = ["Dog", "Cat", "Fly", "Mouse", "Earthworm"]
    number_of_animals = [10, 40, 30, 5, 15]
    Explode = [0, 0, 0, 0.5, 0]
    
    plt.pie(number_of_animals, explode=Explode, labels=animals, shadow=True, startangle=45)
    plt.axis('equal')
    plt.legend(title = "List of Firms")
    # plt.show()
    
    #Example of creating a simple bar chart and stacking them together
    #==============================================================================================================
    fruits = ["apple", "orange", "banana", "pear", "melon", "cucumber"]
    dog = [97, 0, 59, 81, 77, 92]
    cat = [88, 61, 80, 40, 62, 52]
    mouse = [54, 62, 77, 54, 71, 98]
    index = np.arange(6)
    width = 0.03 
       
    plt.bar(index, dog, width, color="aqua", label="Dog")
    plt.bar(index + width, cat, width, color="green", label="Cat")
    plt.bar(index + (width*2), mouse, width, color="blue", label="Mouse") 
    
    plt.title("Stacked Bar Graph Example")
    plt.xlabel("Animals")
    plt.ylabel("Fruits Eaten")  
    
    plt.xticks(index + width/2, fruits)
    plt.legend()
    # plt.show()
    
    #Example of creating a simple bar chart and stacking them together
    #==============================================================================================================
    
    x = np.random.randn(10000)

    plt.hist(x, 10) #To divide the data into 10 different bins
    plt.title("Histogram Example")
    plt.xlabel("Random Data")
    plt.ylabel("Frequency")
    # plt.show()
    
    #Example of creating a 3D projection using matplotlib
    #==============================================================================================================
    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib
    
    x = np.linspace(-5, 5, 50)
    y = np.linspace(-5, 5, 50)
    X, Y = np.meshgrid(x, y)
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R)

    figure = plt.figure(1, figsize = (12, 4))
    subplot3d = plt.subplot(111, projection='3d')
    surface = subplot3d.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=matplotlib.cm.coolwarm, linewidth=0.1)
    # plt.show()
    
    #Example of creating a scatterplot
    #==============================================================================================================
    from numpy.random import rand
    for color in ['red', 'green', 'blue']:
        n = 100
        xx, yy = rand(2, n)
        scale = 500.0 * rand(n) ** 5
    
    plt.scatter(xx, yy, s=scale, c=color, alpha=0.3, edgecolors ='blue')
    plt.grid(True)
    # plt.show()
    
    #Example of creating a Subplot
    #==============================================================================================================
    plt.subplot(2,1,1) 
    plt.plot(range(12)) 
    plt.subplot(2,1,2, facecolor='red') 
    plt.plot(range(12)) 
    # plt.show()
    
    #OR
 
    import math 
    x = np.arange(0, math.pi*2, 0.09) 
    fig=plt.figure() 
    axes1 = fig.add_axes([0.1, 0.1, 0.9, 0.9]) 
    axes2 = fig.add_axes([0.62, 0.62, 0.3, 0.3]) 
    y = np.sin(x) 
    axes1.plot(x, y, 'b') 
    axes2.plot(x,np.cos(x),'r') 
    axes1.set_title('sine') 
    axes2.set_title("cosine") 
    # plt.show()
    
    #Example of plotting an image using matplotlib
    # ===========================================================================================================
    import matplotlib.image as mpimg
    path = '<Enter an Image Path>'
    img = mpimg.imread(path)
    # plt.imshow(img)

