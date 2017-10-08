import matplotlib.pyplot as plt
from matplotlib.pyplot import savefig

ax = plt.axes()
ax.arrow(0, 0,  0.5,  0.0, head_width=0.02, head_length=0.05,
         fc='k', ec='k', shape='full', length_includes_head=True)
ax.arrow(0, 0,  0.5,  0.5, head_width=0.02, head_length=0.05,
         fc='k', ec='k', shape='full', length_includes_head=True)
ax.arrow(0, 0,  0.0,  0.5, head_width=0.02, head_length=0.05,
         fc='k', ec='k', shape='full', length_includes_head=True)
ax.arrow(0, 0, -0.5,  0.5, head_width=0.02, head_length=0.05,
         fc='k', ec='k', shape='full', length_includes_head=True)
ax.arrow(0, 0, -0.5,  0.0, head_width=0.02, head_length=0.05,
         fc='k', ec='k', shape='full', length_includes_head=True)
ax.arrow(0, 0, -0.5, -0.5, head_width=0.02, head_length=0.05,
         fc='k', ec='k', shape='full', length_includes_head=True)
ax.arrow(0, 0,  0.0, -0.5, head_width=0.02, head_length=0.05,
         fc='k', ec='k', shape='full', length_includes_head=True)
ax.arrow(0, 0,  0.5, -0.5, head_width=0.02, head_length=0.05,
         fc='k', ec='k', shape='full', length_includes_head=True)
plt.text(0.05, 0.02, r'$\bf {c}_1$', size=20)
plt.text(0.45, 0.02, r'$\bf {c}_2$', size=20)
plt.text(0.02, 0.45, r'$\bf {c}_3$', size=20)
plt.text(-0.45, 0.02, r'$\bf {c}_4$', size=20)
plt.text(0.02, -0.45, r'$\bf {c}_5$', size=20)

plt.text(0.45, 0.43, r'$\bf {c}_6$', size=20)
plt.text(-0.45, 0.45, r'$\bf {c}_7$', size=20)
plt.text(-0.43, -0.45, r'$\bf {c}_8$', size=20)
plt.text(0.45, -0.43, r'$\bf {c}_9$', size=20)
plt.text(-0.03, -0.023, r'$\bullet$', size=30)
plt.xlim([-0.5, 0.5])
plt.ylim([-0.5, 0.5])
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])
savefig(r'D2Q9TRT.eps', bbox_inches='tight')
plt.show()
