from client import AgenticCrmRelationshipGraphOrchestratorClient

def main():
    client = AgenticCrmRelationshipGraphOrchestratorClient()
    res = client.orchestrate_deal_graph(["buyer@bigcorp.com", "cto@bigcorp.com"], "TECHNICAL_REVIEW")
    print(f"Deal Value: ${res['synced_deal_value_usd']}")
    print(f"Next Best Step: {res['next_best_step']}")

if __name__ == "__main__":
    main()
