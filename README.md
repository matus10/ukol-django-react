Úkol k vypracování v rámci pohovoru.

Zadání:

1. Vytvořte jednoduchý datový model obsahující 4 základní entity: Klient, Účet, Transakce a Balance. - HOTOVO

2. Naznačte základní sadu atributů v jednotlivých tabulkách, kardinalitu, primární/cizí klíče, apod. - HOTPVP

3. V tabulce transakcí se bude vyskytovat TYP_TRANSAKCE, který bude odkazovat do číselníku typů transakcí. -HOTOVO

4. Předpokládejte, že tabulka BALANCE obsahuje denní snímky nesoucí informaci o výši jednotlivých komponent pohledávky (jistina, úrok, poplatky) na konci dne. - HOTOVO

5. Postavte dotaz, který vybere všechny klienty (např. id_klient, jméno a příjmení) pro něž bude platit, že suma jistin všech jejich účtů na konci měsíce bude větší než číslo c.

6. Postavte dotaz, který zobrazí 10 klientů s maximální celkovou výší pohledávky (suma všech pohledávek klienta) k ultimu měsíce a tuto na konci řádku vždy zobrazte.


Řešení:

2. Kardinalita:
    Klient : Účet = 1:N
    Účet : Balance = 1:N
    Účet : Transakce = 1:N
    Typ transakce : Transakce = 1:N

Dotazy pro vypsání výsledků z databáze SQLite (Testováno v programu DB Browser)
5. 
    SELECT
    "api_client"."id_client",
    "api_client"."first_name",
    "api_client"."last_name"
    FROM "api_client"
    JOIN "api_account"
    ON "api_account"."client_id" = "api_client"."id_client"
    JOIN "api_balance"
    ON "api_balance"."account_id" = "api_account"."id"
    WHERE "api_balance"."snapshot_date" = "2026-03-13"
    GROUP BY
    "api_client"."id_client",
    "api_client"."first_name",
    "api_client"."last_name"
    HAVING SUM("api_balance"."principal_amount") > c;

6. 
    SELECT 
    "api_client"."id_client",
    "api_client"."first_name",
    "api_client"."last_name",
    SUM("api_balance"."principal_amount" + "api_balance"."interest_amount" + "api_balance"."fee_amount")
    AS "total_balance"
    FROM "api_client"
    JOIN "api_account"
    ON "api_account"."client_id" = "api_client"."id_client"
    JOIN "api_balance"
    ON "api_balance"."account_id" = "api_account"."id"
    WHERE "api_balance"."snapshot_date" = "2026-03-13"
    GROUP BY
    "api_client"."id_client",
    "api_client"."first_name",
    "api_client"."last_name"
    LIMIT 10;