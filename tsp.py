import itertools
import networkx as nx
import matplotlib.pyplot as plt


def hitung_total_jarak(rute, matriks_jarak):
    total_jarak = 0
    for i in range(len(rute) - 1):
        total_jarak += matriks_jarak[rute[i]][rute[i + 1]]
    return total_jarak


def selesaikan_tsp(matriks_jarak):
    jumlah_lokasi = len(matriks_jarak)
    daftar_node = list(range(1, jumlah_lokasi))

    jarak_minimum = float('inf')
    rute_terbaik = []

    # Mencoba semua kemungkinan rute (brute-force)
    for permutasi in itertools.permutations(daftar_node):
        rute_saat_ini = [0] + list(permutasi) + [0]
        jarak_saat_ini = hitung_total_jarak(rute_saat_ini, matriks_jarak)

        if jarak_saat_ini < jarak_minimum:
            jarak_minimum = jarak_saat_ini
            rute_terbaik = rute_saat_ini

    return rute_terbaik, jarak_minimum


# =====================================================================
# SILAKAN UBAH ANGKA JARAK ANTAR LOKASI DI SINI (dalam km)
# =====================================================================
matriks_jarak = [
    [0,  4,  9, 12,  7,  5],  # Dapur Utama
    [4,  0,  6,  4,  3,  8],  # Kos A
    [9,  6,  0,  8,  5,  6],  # Kos B
    [12, 4,  8,  0,  3,  2],  # Kos C
    [7,  3,  5,  3,  0,  4],  # Kos D
    [5,  8,  6,  2,  4,  0],  # Kos E
]

nama_lokasi = ["Dapur Utama", "Kos A", "Kos B", "Kos C", "Kos D", "Kos E"]
n = len(nama_lokasi)

# Menjalankan algoritma TSP
rute_terbaik_indeks, jarak_minimum = selesaikan_tsp(matriks_jarak)
rute_dengan_nama = [nama_lokasi[i] for i in rute_terbaik_indeks]

print("=== HASIL OPTIMALISASI RUTE TSP ===")
print("Rute Perjalanan Terbaik:", " -> ".join(rute_dengan_nama))
print(f"Total Jarak Minimum: {jarak_minimum} km\n")

# ==========================================
# VISUALISASI GRAF JARINGAN (SPRING LAYOUT)
# ==========================================
G = nx.DiGraph()

for i in range(n):
    for j in range(n):
        if i != j and matriks_jarak[i][j] > 0:
            G.add_edge(nama_lokasi[i], nama_lokasi[j], weight=matriks_jarak[i][j])

posisi_node = nx.spring_layout(G, seed=42)

plt.figure(figsize=(10, 8))
plt.title("Visualisasi Rute TSP - Model Jaringan Bebas", fontsize=13, fontweight='bold', pad=20)

# 1. Garis latar belakang putus-putus untuk semua jalur
garis_latar_belakang = [
    (nama_lokasi[i], nama_lokasi[j])
    for i in range(n) for j in range(i + 1, n)
    if matriks_jarak[i][j] > 0 or matriks_jarak[j][i] > 0
]
nx.draw_networkx_edges(G, posisi_node, edgelist=garis_latar_belakang, width=1.2,
                       edge_color='gray', style='dashed', alpha=0.6, arrows=False)

# 2. Rute optimal: panah merah
garis_rute_optimal = [
    (rute_dengan_nama[i], rute_dengan_nama[i + 1])
    for i in range(len(rute_dengan_nama) - 1)
]
nx.draw_networkx_edges(G, posisi_node, edgelist=garis_rute_optimal, width=2.5, edge_color='red',
                       arrowstyle="-|>", arrowsize=20,
                       min_target_margin=18, min_source_margin=18)

# 3. Node dan label nama
nx.draw_networkx_nodes(G, posisi_node, node_size=2000, node_color='#c2f0c2',
                       edgecolors='black', linewidths=1.5)
nx.draw_networkx_labels(G, posisi_node, font_size=9, font_weight='bold')

# 4. Label jarak di setiap garis
label_jarak = {
    (nama_lokasi[i], nama_lokasi[j]): matriks_jarak[i][j]
    for i in range(n) for j in range(n) if matriks_jarak[i][j] > 0
}
nx.draw_networkx_edge_labels(G, posisi_node, edge_labels=label_jarak, font_size=8,
                             font_color='darkblue',
                             bbox=dict(boxstyle='round,pad=0.2', ec='none', fc='white', alpha=0.8))

plt.axis('off')
plt.tight_layout()
plt.show()
