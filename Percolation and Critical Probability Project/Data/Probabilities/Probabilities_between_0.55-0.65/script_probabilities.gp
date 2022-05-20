set term pdf
set out "Probabilidad_de_que_exista_un_cluster_percolante_en_función_de_p_y_L"
set xlabel "Probabilidad de llenado"  
set ylabel "s(p,L)"
set title " Probabilidad de que aparezca un cluster percolante en función de p y L"
set key left top

# plot "datos32.txt" u 1:2 w l lw 2 t "L = 32", "datos64.txt" u 1:2 w l lw 2 t "L = 64", "datos128.txt" u 1:2 w l lw 2 t "L = 128", "datos256.txt" u 1:2 w l lw 2 t "L = 256"
plot "datos32.txt" u 1:2:3 w yerrorlines lw 2 t "L = 32", "datos64.txt" u 1:2:3 w yerrorlines lw 2 t "L = 64", "datos128.txt" u 1:2:3 w yerrorlines lw 2 t "L = 128", "datos256.txt" u 1:2:3 w yerrorlines lw 2 t "L = 256"