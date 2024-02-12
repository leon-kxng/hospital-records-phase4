async function fetchData(entity) {
    try {
        const response = await fetch(`https://hospital-records.replit.app/${entity}s`);
        if (!response.ok) {
            throw new Error(`Failed to fetch ${entity}s: ${response.statusText}`);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error(`Error fetching ${entity}s:`, error);
        throw error;
    }
}

export default fetchData;
