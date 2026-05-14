# Define uma versão mínima realista e estável
cmake_minimum_required(VERSION 4.0)

# Nome geral do seu projeto/repositório
project(Listas_Algoritmos C)

# Define o padrão C23 (certifique-se de que seu compilador GCC/Clang suporta essa versão recente)
set(CMAKE_C_STANDARD 23)

# Cria um executável ISOLADO para o primeiro problema
add_executable(boy_or_girl boy_or_girl.c
        twins.c
        worms.c
        business_trip.c
        less_or_equals.c)

# Cria um executável ISOLADO para o segundo problema
add_executable(dragoes dragoes.c)

add_executable(string string.c)

add_executable(matriz Beautiful_Matrix.c)

add_executable(Maximum_in_Table Maximum_in_Table.c)
add_executable(twins twins.c)
add_executable(business_trip business_trip.c)
add_executable(less_or_equals less_or_equals.c)
