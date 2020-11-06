set terminal png

# task 1_1
set output "figures/task1_1/figure_111.png"
set title "cwnd of app (a)"
set xlabel "Time (seconds)"
set ylabel "cwnd size"
plot "./outputs/task1_1/app1.cwnd" using 1:2 with lines title "App (a) cwnd size" lw 2

set output "figures/task1_1/figure_112.png"
set title "Throughput of app (a)"
set xlabel "Time (seconds)"
set ylabel "Throughput (Mbps)"
plot "./outputs/task1_1/app1.rx" using 1:2 with lines title "App (a) cwnd size" lw 2

# task 1_2
set output "figures/task1_2/figure_121.png"
set title "cwnd of apps (a), (b)"
set xlabel "Time (seconds)"
set ylabel "cwnd size"
plot "./outputs/task1_2/app1.cwnd" using 1:2 with lines title "App (a)" lw 2, "./outputs/task1_2/app2.cwnd" using 1:2 with lines title "App (b)" lw 2

set output "figures/task1_2/figure_122.png"
set title "Throughput of apps (a), (b)"
set xlabel "Time (seconds)"
set ylabel "Throughput (Mbps)"
plot "./outputs/task1_2/app1.rx" using 1:2 with lines title "App (a)" lw 2, "./outputs/task1_2/app2.rx" using 1:2 with lines title "App (b)" lw 2

# task 1_3
set output "figures/task1_3/figure_131.png"
set title "cwnd of apps (a), (b), (c)"
set xlabel "Time (seconds)"
set ylabel "cwnd size"
plot "./outputs/task1_3/app1.cwnd" using 1:2 with lines title "App (a)" lw 2, "./outputs/task1_3/app2.cwnd" using 1:2 with lines title "App (b)" lw 2, "./outputs/task1_3/app3.cwnd" using 1:2 with lines title "App (c)" lw 2

set output "figures/task1_3/figure_132.png"
set title "Throughput of apps (a), (b), (c)"
set xlabel "Time (seconds)"
set ylabel "Throughput (Mbps)"
plot "./outputs/task1_3/app1.rx" using 1:2 with lines title "App (a)" lw 2, "./outputs/task1_3/app2.rx" using 1:2 with lines title "App (b)" lw 2, "./outputs/task1_3/app3.rx" using 1:2 with lines title "App (c)" lw 2

# task 1_4
set output "figures/task1_4/figure_141.png"
set title "cwnd of apps (a), (b), (c) with error rate"
set xlabel "Time (seconds)"
set ylabel "cwnd size"
plot "./outputs/task1_4/app1.cwnd" using 1:2 with lines title "App (a)" lw 2, "./outputs/task1_4/app2.cwnd" using 1:2 with lines title "App (b)" lw 2, "./outputs/task1_4/app3.cwnd" using 1:2 with lines title "App (c)" lw 2

set output "figures/task1_4/figure_142.png"
set title "Throughput of apps (a), (b), (c) with error rate"
set xlabel "Time (seconds)"
set ylabel "Throughput (Mbps)"
plot "./outputs/task1_4/app1.rx" using 1:2 with lines title "App (a)" lw 2, "./outputs/task1_4/app2.rx" using 1:2 with lines title "App (b)" lw 2, "./outputs/task1_4/app3.rx" using 1:2 with lines title "App (c)" lw 2

# task 2_1_1
set output "figures/task2_1_1/figure_211_cwnd.png"
set title "cwnd of apps (a), (b), (c) with alternative adder"
set xlabel "Time (seconds)"
set ylabel "cwnd size"
plot "./outputs/task2_1_1/app1.cwnd" using 1:2 with lines title "App (a)" lw 2, "./outputs/task2_1_1/app2.cwnd" using 1:2 with lines title "App (b)" lw 2, "./outputs/task2_1_1/app3.cwnd" using 1:2 with lines title "App (c)" lw 2

set output "figures/task2_1_1/figure_211_throughput.png"
set title "Throughput of apps (a), (b), (c) with alternative adder"
set xlabel "Time (seconds)"
set ylabel "Throughput (Mbps)"
plot "./outputs/task2_1_1/app1.rx" using 1:2 with lines title "App (a)" lw 2, "./outputs/task2_1_1/app2.rx" using 1:2 with lines title "App (b)" lw 2, "./outputs/task2_1_1/app3.rx" using 1:2 with lines title "App (c)" lw 2

# task 2_1_2
set output "figures/task2_1_2/figure_212_cwnd.png"
set title "cwnd of apps (a), (b), (c) without recovery"
set xlabel "Time (seconds)"
set ylabel "cwnd size"
plot "./outputs/task2_1_2/app1.cwnd" using 1:2 with lines title "App (a)" lw 2, "./outputs/task2_1_2/app2.cwnd" using 1:2 with lines title "App (b)" lw 2, "./outputs/task2_1_2/app3.cwnd" using 1:2 with lines title "App (c)" lw 2

set output "figures/task2_1_2/figure_212_throughput.png"
set title "Throughput of apps (a), (b), (c) without recovery"
set xlabel "Time (seconds)"
set ylabel "Throughput (Mbps)"
plot "./outputs/task2_1_2/app1.rx" using 1:2 with lines title "App (a)" lw 2, "./outputs/task2_1_2/app2.rx" using 1:2 with lines title "App (b)" lw 2, "./outputs/task2_1_2/app3.rx" using 1:2 with lines title "App (c)" lw 2

# task 2_2_veno
set output "figures/task2_2_veno/figure_221_cwnd.png"
set title "cwnd of apps (a), (b), (c) with TCP Veno"
set xlabel "Time (seconds)"
set ylabel "cwnd size"
plot "./outputs/task2_2_veno/app1.cwnd" using 1:2 with lines title "App (a)" lw 2, "./outputs/task2_2_veno/app2.cwnd" using 1:2 with lines title "App (b)" lw 2, "./outputs/task2_2_veno/app3.cwnd" using 1:2 with lines title "App (c)" lw 2

set output "figures/task2_2_veno/figure_221_throughput.png"
set title "Throughput of apps (a), (b), (c) with TCP Veno"
set xlabel "Time (seconds)"
set ylabel "Throughput (Mbps)"
plot "./outputs/task2_2_veno/app1.rx" using 1:2 with lines title "App (a)" lw 2, "./outputs/task2_2_veno/app2.rx" using 1:2 with lines title "App (b)" lw 2, "./outputs/task2_2_veno/app3.rx" using 1:2 with lines title "App (c)" lw 2

# task 2_2_yeah
set output "figures/task2_2_yeah/figure_221_cwnd.png"
set title "cwnd of apps (a), (b), (c) with TCP Yeah"
set xlabel "Time (seconds)"
set ylabel "cwnd size"
plot "./outputs/task2_2_yeah/app1.cwnd" using 1:2 with lines title "App (a)" lw 2, "./outputs/task2_2_yeah/app2.cwnd" using 1:2 with lines title "App (b)" lw 2, "./outputs/task2_2_yeah/app3.cwnd" using 1:2 with lines title "App (c)" lw 2

set output "figures/task2_2_yeah/figure_221_throughput.png"
set title "Throughput of apps (a), (b), (c) with TCP Yeah"
set xlabel "Time (seconds)"
set ylabel "Throughput (Mbps)"
plot "./outputs/task2_2_yeah/app1.rx" using 1:2 with lines title "App (a)" lw 2, "./outputs/task2_2_yeah/app2.rx" using 1:2 with lines title "App (b)" lw 2, "./outputs/task2_2_yeah/app3.rx" using 1:2 with lines title "App (c)" lw 2
