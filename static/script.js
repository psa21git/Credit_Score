function predict() {
    const payload = {
        Age: document.getElementById("Age").value,
        Annual_Income: document.getElementById("Annual_Income").value,
        Monthly_Inhand_Salary: document.getElementById("Monthly_Inhand_Salary").value,
        Num_Bank_Accounts: document.getElementById("Num_Bank_Accounts").value,
        Num_Credit_Card: document.getElementById("Num_Credit_Card").value,
        Interest_Rate: document.getElementById("Interest_Rate").value,
        Num_of_Loan: document.getElementById("Num_of_Loan").value,
        Type_of_Loan: document.getElementById("Type_of_Loan").value,
        Delay_from_due_date: document.getElementById("Delay_from_due_date").value,
        Num_of_Delayed_Payment: document.getElementById("Num_of_Delayed_Payment").value,
        Changed_Credit_Limit: document.getElementById("Changed_Credit_Limit").value,
        Num_Credit_Inquiries: document.getElementById("Num_Credit_Inquiries").value,
        Credit_Mix: document.getElementById("Credit_Mix").value,
        Outstanding_Debt: document.getElementById("Outstanding_Debt").value,
        Credit_Utilization_Ratio: document.getElementById("Credit_Utilization_Ratio").value,
        Credit_History_Age: document.getElementById("Credit_History_Age").value,
        Payment_of_Min_Amount: document.getElementById("Payment_of_Min_Amount").value,
        Total_EMI_per_month: document.getElementById("Total_EMI_per_month").value,
        Amount_invested_monthly: document.getElementById("Amount_invested_monthly").value,
        Payment_Behaviour: document.getElementById("Payment_Behaviour").value,
        Monthly_Balance: document.getElementById("Monthly_Balance").value,
        Occupation: document.getElementById("Occupation").value,
        Month: document.getElementById("Month").value
    };

    fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerText =
            "Credit Status: " + data.credit_status +
            " | Default Risk: " + data.default_probability;
    })
    .catch(err => {
        document.getElementById("result").innerText = "Error occurred!";
        console.error(err);
    });
}
