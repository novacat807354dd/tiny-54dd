if __name__=="__main__":
    parser=argparse.ArgumentParser(description="Tiny embedding similarity search.")
    parser.add_argument("embeddings", help="Path to CSV embeddings file")
    parser.add_argument("query", help="Query vector as comma-separated numbers")
    parser.add_argument("-k", type=int, default=5, help="Number of top results")
    args=parser.parse_args()
    query=[float(x) for x in args.query.split(',')]
    embeddings=read_embeddings(args.embeddings)
    results=search(query, embeddings, args.k)
    for idx,(id,sim) in enumerate(results,1):
        print(f"{idx}. {id} (cosine={sim:.4f})")