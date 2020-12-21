set terminal png

# task 1_2
set output "figures/figure_12.png"
set title "Throughput of flow on 2.4GHz"
set xlabel "x coordinate of A"
set ylabel "Throughput"
plot "./outputs/task12/output" using 1:2 with lines title "throughput" lw 2

# task 1_3
set output "figures/figure_13.png"
set title "Throughput of flow on 5GHz"
set xlabel "x coordinate of A"
set ylabel "Throughput"
plot "./outputs/task13/output" using 1:2 with lines title "throughput" lw 2
