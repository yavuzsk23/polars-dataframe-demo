import polars as pl
from loguru import logger


def run_polars_demo():
    logger.info("Initializing Polars engine (Rust-based backend)...")

    # 1. Create a sample dataset (a Polars table is called a DataFrame)
    data = {
        "agent_name": ["Yavuz", "Mete", "Hakan", "Asena", "Oguz"],
        "department": ["Security", "Backend", "Security", "Frontend", "Backend"],
        "code_speed_seconds": [120, 85, 150, 95, 110],
        "german_level": ["B1", "A2", "B2", "A1", "B1"],
    }

    df = pl.DataFrame(data)
    logger.success("Dataset loaded into a Polars DataFrame.")

    print("\n--- FULL DATA TABLE ---")
    print(df)

    # 2. Filter: only rows from the Security department
    logger.info("Filtering: department == 'Security'")
    security_team = df.filter(pl.col("department") == "Security")

    print("\n--- SECURITY TEAM ---")
    print(security_team)

    # 3. Group by department and compute average code speed per group
    logger.info("Grouping by department, computing average speed...")
    avg_by_department = (
        df.group_by("department")
        .agg(pl.col("code_speed_seconds").mean().alias("avg_speed_seconds"))
        .sort("avg_speed_seconds")
    )

    print("\n--- AVERAGE SPEED BY DEPARTMENT (fastest first) ---")
    print(avg_by_department)

    # 4. Overall average code speed across the whole team
    overall_avg = df.select(pl.col("code_speed_seconds").mean()).item()
    logger.success(f"Analysis complete! Team average code speed: {overall_avg:.2f} seconds.")


if __name__ == "__main__":
    run_polars_demo()
