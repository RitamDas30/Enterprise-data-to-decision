import os

def persist_kpis(kpis: dict, output_dir="storage/warehouse/analytics"):
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "kpis.txt")

    with open(path, "w") as f:
        for k, v in kpis.items():
            f.write(f"{k}: {v}\n")

    return path
