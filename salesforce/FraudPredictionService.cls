public class FraudPredictionService {
    @future (callout=true)
    public static void sendFraudCheck(String orderId, Decimal amount, Integer accountAge, Integer txnCount, String deviceType) {
        HttpRequest req = new HttpRequest();
        req.setEndpoint('https://your-flask-api-url/predict');
        req.setMethod('POST');
        req.setHeader('Content-Type', 'application/json');

        Map<String, Object> body = new Map<String, Object>();
        body.put('transaction_amount', amount);
        body.put('account_age_days', accountAge);
        body.put('num_previous_transactions', txnCount);
        body.put('device_type', deviceType);

        req.setBody(JSON.serialize(body));

        Http http = new Http();
        HttpResponse res = http.send(req);

        if (res.getStatusCode() == 200) {
            Map<String, Object> result = (Map<String, Object>)JSON.deserializeUntyped(res.getBody());
            System.debug('Fraud Score: ' + result.get('fraud_score'));
        } else {
            System.debug('Fraud API call failed with status: ' + res.getStatusCode());
        }
    }
}
