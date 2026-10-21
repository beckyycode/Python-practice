#!/usr/bin/env python3
"""
debruijn.py - build a simple De Bruijn graph from short reads and assemble contigs.
 
Nodes are k-mers. An arrow connects two k-mers when the last k-1 bases of the
first match the first k-1 bases of the second (same convention as lecture).
 
Usage:
  python3 debruijn.py -k 3 ATGGCG GGCGTA CGTACA
  python3 debruijn.py -k 3 ATGGCG:20 GCGAAC:1    (":20" = read seen 20 times)
"""
import argparse
from collections import Counter
 
def parse_reads(items):
    reads = []
    for item in items:
        seq, _, n = item.partition(":")
        reads.append((seq.upper(), int(n) if n else 1))
    return reads
 
def count_kmers(reads, k):
    counts = Counter()
    for seq, n in reads:
        if len(seq) < k:
            print(f"Warning: read {seq} is shorter than k={k} and was skipped")
        for i in range(len(seq) - k + 1):
            counts[seq[i:i + k]] += n
    return counts
 
def build_graph(kmers):
    out_edges = {v: [] for v in kmers}
    in_edges = {v: [] for v in kmers}
    for a in kmers:
        for b in kmers:
            if a[1:] == b[:-1]:          # last k-1 of a == first k-1 of b
                out_edges[a].append(b)
                in_edges[b].append(a)
    return out_edges, in_edges
 
def find_contigs(kmers, out_edges, in_edges):
    """Contigs = longest paths that don't pass through a branch point."""
    def simple(v):  # exactly one arrow in and one arrow out
        return len(in_edges[v]) == 1 and len(out_edges[v]) == 1
    paths, used = [], set()
    for v in kmers:
        if not simple(v):
            if not in_edges[v] and not out_edges[v]:
                paths.append([v])            # k-mer with no connections
            for w in out_edges[v]:
                path = [v, w]
                while simple(w):
                    w = out_edges[w][0]
                    path.append(w)
                paths.append(path)
            used.update(p for path in paths for p in path)
    for v in kmers:                          # loops with no way in or out
        if v not in used and simple(v):
            path, w = [v], out_edges[v][0]
            while w != v:
                path.append(w)
                w = out_edges[w][0]
            path.append(v)
            used.update(path)
            paths.append(path)
    return paths
 
def spell(path):
    return path[0] + "".join(kmer[-1] for kmer in path[1:])
 
def main():
    parser = argparse.ArgumentParser(description="Simple De Bruijn graph assembler")
    parser.add_argument("-k", type=int, required=True, help="k-mer length")
    parser.add_argument("reads", nargs="+", help="reads, optionally READ:COUNT")
    args = parser.parse_args()
 
    reads = parse_reads(args.reads)
    counts = count_kmers(reads, args.k)
    kmers = list(counts)                 # order of first appearance in the reads
    out_edges, in_edges = build_graph(kmers)
 
    total = sum(counts.values())
    print(f"\n{args.k}-mers: {total} total, {len(kmers)} unique")
    print("-" * 40)
    for v in kmers:
        print(f"{v}  seen {counts[v]}x")
 
    paths = find_contigs(kmers, out_edges, in_edges)
 
    print("\nGraph")
    print("-" * 40)
    for path in paths:
        if len(path) == 1:
            note = "   (no connections)"
        elif path[-1] == path[0]:
            note = "   (loop)"
        else:
            note = ""
        print(" -> ".join(path) + note)
    branches = [v for v in kmers if len(out_edges[v]) > 1 or len(in_edges[v]) > 1]
    print("\nBranch points (more than one arrow in or out): " +
          (", ".join(branches) if branches else "none"))
 
    print("\nContigs")
    print("-" * 40)
    for i, path in enumerate(paths, 1):
        low = min(counts[v] for v in path)
        print(f"Contig {i}: {spell(path)}  (length {len(spell(path))}, lowest k-mer count {low})")
    print()
 
if __name__ == "__main__":
    main()