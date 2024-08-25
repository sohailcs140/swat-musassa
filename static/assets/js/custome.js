function send_emails_once_in_day(){
    document.getElementById('notification-container').addEventListener('htmx:beforeRequest', function(event) {
    
        if (!shouldTrigger()) {  
            event.preventDefault();
        }
    });
    
    function shouldTrigger() {
        
        const now = new Date();
        const lastTriggered = localStorage.getItem('lastTriggered');
        const oneDay = 24 * 60 * 60 * 1000;
    
        if (!lastTriggered || (now - new Date(lastTriggered)) > oneDay) {
            localStorage.setItem('lastTriggered', now);
            return true;
        }
    
        return false;
    }
}



send_emails_once_in_day()


