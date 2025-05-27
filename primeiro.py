from matplotlib import pyplot as plt
df['total'].plot(kind='line', figsize=(8, 4), title= 'Total de Usuarios',)
plt.gca().spines[['right']].set_visible(False)
