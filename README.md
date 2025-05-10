# Маятник Дубошинского: аналитическое и численное исследование

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Pendulum_animation.gif/220px-Pendulum_animation.gif" width="250" align="right">

## Теоретическая часть

### 1. Постановка задачи
Маятник Дубошинского – механическая система, представляющая собой материальную точку массой _m_, подвешенную на невесомом нерастяжимом стержне длинной _l_ во вращающейся системе отсчёта с угловой скоростью **Ω**. Это обобщение сферического маятника, учитывающее влияние вращения системы на динамику.

Основные особенности:

Имеет две степени свободы: угол отклонения θ и азимутальный угол φ
Учитывает угловую скорость вращения системы Ω
Описывается системой нелинейных дифференциальных уравнений
Демонстрирует сложные динамические режимы: от регулярных колебаний до хаоса

Ключевое отличие от обычного маятника – наличие дополнительных членов в уравнениях движения, учитывающих вращение системы.

![SCHEMATIC_OF_THE_DOUBOCHINSKI_PENDULUM](https://github.com/user-attachments/assets/70f365ed-e1d0-470f-a711-574cc4defa5b)


### 2. Уравнения движения
Вывод из принципа Даламбера-Лагранжа:

```math
\begin{cases}
\ddot{θ} - \sinθ\cosθ(φ̇ + Ω)^2 + \frac{g}{l}\sinθ = 0 \\
\frac{d}{dt}(\sin²θ(φ̇ + Ω)) = 0
\end{cases}
```

### 3. Основные свойства
1. **Циклический интеграл**:  
   `p_φ = ml²sin²θ(φ̇ + Ω) = const`

2. **Энергетический интеграл**:  
   `E = 1/2 ml²(θ̇² + sin²θ(φ̇+Ω)²) - mglcosθ`

3. **Критическая скорость**:  
   `Ω_cr = √(g/l)` - точка бифуркации

## Численная реализация

### 1. Генерация расчетной сетки
```python
# meshing.py
import gmsh
gmsh.initialize()
gmsh.model.add("pendulum")

# Создание геометрии
lc = 0.1
gmsh.model.geo.addPoint(0, 0, 0, lc, 1) 
# ... другие точки и линии ...

gmsh.model.mesh.generate(3)
gmsh.write("mesh.msh")
```

**Назначение**: Построение 3D сетки для конечно-элементного анализа.

### 2. Моделирование динамики
```python
# dynamics.py
import numpy as np

def euler_step(theta, phi, dt):
    # Ваша реализация метода Эйлера
    theta_new = theta + dtheta_dt(theta, phi) * dt
    phi_new = phi + dphi_dt(theta, phi) * dt
    return theta_new, phi_new
```

**Метод**: Явный метод Эйлера с постоянным шагом.

### 3. Визуализация
```python
# visualization.py
from matplotlib.animation import FuncAnimation

def create_animation(theta_vals, phi_vals):
    fig, ax = plt.subplots()
    line, = ax.plot([], [], 'o-')
    
    def animate(i):
        x = [0, np.sin(theta_vals[i])]
        y = [0, -np.cos(theta_vals[i])]
        line.set_data(x, y)
        return line,
    
    anim = FuncAnimation(fig, animate, frames=len(theta_vals))
    anim.save('pendulum.gif')
```

**Функционал**: Создание 2D анимации движения.

## Результаты

### Пример фазового портрета
![Фазовый портрет](https://www.researchgate.net/publication/334455992/figure/fig1/AS:781522971934720@1563984697496/Nonlinear-pendulum-trajectories.png)

### Ключевые наблюдения
1. При Ω < Ω_cr - регулярные колебания
2. При Ω ≈ Ω_cr - бифуркация Андронова-Хопфа
3. При Ω > Ω_cr - хаотические режимы

## Запуск проекта

1. Установить зависимости:
```bash
pip install gmsh numpy matplotlib
```

2. Последовательно выполнить:
```bash
python meshing.py
python dynamics.py
python visualization.py
```

© 2025 Проект по аналитической механике  
