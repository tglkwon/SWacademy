import matplotlib.pyplot as plt
#import matplotlib.pylab as plt
plt.plot([1,2,3],[4,5,6])
plt.title('title')
plt.figure(figsize=(5,5))
plt.axes((0,0,0.5,0.5))
plt.title('sun')
plt.axes((0.5,0.5,.5,.5))
plt.plot([1,2,3,5],[1,4,5,6])
plt.title('moon')

# plt.axes(share=True)
plt.subplot(1,2,1)
plt.subplot(1,2,2)
plt.title('sun')

# fig, (ax1, ax2) = plt.subplot(1,2)
# ax2.set_title('moon')
# ax1.set_title('sun')

plt.show()


def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return fibonacci(n-1) + fibonacci(n-2)