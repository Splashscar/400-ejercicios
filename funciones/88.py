# Este es el archivo n�mero 88
class felipe_mendieta:
    def c_a_f(self, c):
        return (c * 9/5) + 32

    def f_a_c(self, f):
        return (f - 32) * 5/9

conv = felipe_mendieta()
print("30°C =", conv.c_a_f(30), "°F")
