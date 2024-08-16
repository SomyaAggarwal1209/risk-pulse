document.addEventListener('DOMContentLoaded', () => {
    const riskCircle = document.getElementById('riskCircle');
    const riskText = document.getElementById('riskText');
    const generateReportButton = document.getElementById('generateReportButton');
    const reportSection = document.getElementById('reportSection');
    const reportContent = document.getElementById('reportContent');
    const downloadReportButton = document.getElementById('downloadReportButton');
    const showDetailsButton = document.getElementById('showDetailsButton');
    const riskDetails = document.getElementById('riskDetails');
    const toggleDarkModeButton = document.getElementById('toggleDarkMode');

    // Simulate risk percentage change
    let percentage = 0;
    const targetPercentage = 75;

    const updateRiskPercentage = () => {
        if (percentage < targetPercentage) {
            percentage++;
            riskText.textContent = `${percentage}%`;
            riskCircle.style.background = `conic-gradient(#76ff03 ${percentage}%, #1e1e1e ${percentage}%)`;
            requestAnimationFrame(updateRiskPercentage);
        }
    };

    updateRiskPercentage();

    generateReportButton.addEventListener('click', () => {
        const reportText = `Risk Report:\n\nRisk Percentage: ${percentage}%\nThis is a simulated risk report.`;
        reportContent.textContent = reportText;
        reportSection.style.display = 'block';
        downloadReportButton.style.display = 'inline-block';
    });

    downloadReportButton.addEventListener('click', () => {
        const blob = new Blob([reportContent.textContent], { type: 'text/plain' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'risk_report.txt';
        a.click();
        URL.revokeObjectURL(url);
    });

    showDetailsButton.addEventListener('click', () => {
        riskDetails.style.display = riskDetails.style.display === 'none' ? 'block' : 'none';
    });

    // Initialize charts
    const ctxTrends = document.getElementById('trendsChart').getContext('2d');
    const trendsChart = new Chart(ctxTrends, {
        type: 'line',
        data: {
            labels: ['January', 'February', 'March', 'April', 'May'],
            datasets: [{
                label: 'Risk Trends',
                data: [10, 20, 30, 40, 50],
                backgroundColor: 'rgba(118, 255, 3, 0.2)',
                borderColor: '#76ff03',
                borderWidth: 2
            }]
        }
    });

    const ctxCategory = document.getElementById('categoryChart').getContext('2d');
    const categoryChart = new Chart(ctxCategory, {
        type: 'pie',
        data: {
            labels: ['Operational', 'Financial', 'Compliance'],
            datasets: [{
                label: 'Risk by Category',
                data: [30, 50, 20],
                backgroundColor: ['#76ff03', '#1e1e1e', '#555']
            }]
        }
    });

})
