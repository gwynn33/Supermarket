export async function SendRequest(data,url,method='POST') {
    const response = await fetch (url , {
        method,
        headers : {"Content-Type":"application/json"},
        body : JSON.stringify(data)
    });

    let result = {};
    try {
        result = await response.json();
    } catch {
        result = {success : false , error : "invalid Json response"};
    }
    return {
        success: response.ok && result.success,
        message: result.message,
        error: result.error || (!response.ok ? `HTTP Error ${response.status}` : null),
        status: response.status,
        type : result.type
    }
}