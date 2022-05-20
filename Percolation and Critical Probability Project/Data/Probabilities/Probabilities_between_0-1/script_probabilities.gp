set term pdf
set out "Probabilidad_de_que_exista_un_cluster_percolante.pdf"
set xlabel "Probabilidad de llenado"  
set ylabel "P(p,L)"
set title " Probabilidad de que aparezca un cluster percolante en función de p y L"
plot "datos32.txt" u 1:2 w l lw 2 t "L = 32", "datos64.txt" u 1:2 w l lw 2 t "L = 64", "datos128.txt" u 1:2 w l lw 2 t "L = 128", "datos256.txt" u 1:2 w l lw 2 t "L = 256"
# plot "datos32.txt" u 1:2:3 w yerrorlines lw 2 t "L = 32", "datos64.txt" u 1:2:3 w yerrorlines lw 2 t "L = 64", "datos128.txt" u 1:2:3 w yerrorlines lw 2 t "L = 128", "datos256.txt" u 1:2:3 w yerrorlines lw 2 t "L = 256"
