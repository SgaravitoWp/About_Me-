set term pdf
set out "Tiempo_en_función_del_tamaño_para_diferentes_optimizaciones.pdf"
set xlabel "Tamaño de la matriz"
set ylabel "Tiempo de cómputo (s)"
set title "Tiempo de cómputo en función del tamaño de la matriz con p=0.564146"
set log y
set log x
set key left top
plot "tiempos_con-O0.txt" u 1:3 w lp t "O0", "tiempos_con-O1.txt" u 1:3 w lp t "O1", "tiempos_con-O2.txt" u 1:3 w lp t "O2", "tiempos_con-O3.txt" u 1:3 w lp t "O3"