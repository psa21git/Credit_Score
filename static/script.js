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
        const resultBox = document.getElementById("result");
        resultBox.classList.remove("hidden", "success", "warn", "danger");
        
        let statusClass = "success";
        let icon = "fa-circle-check";
        
        const status = (data.credit_status || "").toString().toLowerCase();
        if (status.includes("poor") || status.includes("bad")) {
            statusClass = "danger";
            icon = "fa-circle-xmark";
        } else if (status.includes("standard") || status.includes("fair")) {
            statusClass = "warn";
            icon = "fa-triangle-exclamation";
        }

        resultBox.classList.add(statusClass);
        resultBox.innerHTML = `
            <div style="font-size: 1.5rem; margin-bottom: 10px;">
                <i class="fa-solid ${icon}"></i> 
                Credit Status: <strong>${data.credit_status}</strong>
            </div>
            <div style="font-size: 0.95rem; font-weight: 500; opacity: 0.8;">
                Estimated Default Risk: ${data.default_probability}
            </div>
        `;
    })
    .catch(err => {
        const resultBox = document.getElementById("result");
        resultBox.classList.remove("hidden", "success", "warn");
        resultBox.classList.add("danger");
        resultBox.innerHTML = `<i class="fa-solid fa-triangle-exclamation"></i> An error occurred while predicting. Please try again.`;
        console.error(err);
    });
}
