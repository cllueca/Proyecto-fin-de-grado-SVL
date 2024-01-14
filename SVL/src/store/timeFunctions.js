import moment from 'moment';

export function getRelativeTime(dateString){
    var fechaTemp = moment(dateString, 'ddd, DD MMM YYYY HH:mm:ss [GMT]');
    const now = moment();
    const diffInDays = now.diff(fechaTemp, 'days');
    if (diffInDays === 0) {
        const diffInHours = now.diff(fechaTemp, 'hours');
        return "Hace " + diffInHours + " horas";
    }
    else if(diffInDays > 31)
    {
        return "Hace mas de un mes";
    }
    else{
        if (diffInDays === 1)
        {
            return "Hace " + diffInDays + " día";
        }
        else
        {
            return "Hace " + diffInDays + " días";
        }
    }
}

export function getFormattedDate(dateString){

    // Con este codigo devuelve: 01/05/2023
        // const fechaAnalizada = moment(dateString, 'ddd, DD MMM YYYY HH:mm:ss [GMT]');
        // const fechaFormateada = fechaAnalizada.format('DD-MM-YYYY');

        // return fechaFormateada;

    // Si quiero que devuelve febreo del 2023, por ejemplo, seria este codigo:
    const fechaTemp = moment(dateString, 'ddd, DD MMM YYYY HH:mm:ss [GMT]');
    const now = moment();
    const diffInDays = now.diff(fechaTemp, 'days');
    
    if (diffInDays === 0) {
        const diffInHours = now.diff(fechaTemp, 'hours');
        if (diffInHours === 0)
        {
            const diffInMins = now.diff(fechaTemp, 'minutes');
            if(diffInMins === 1)
            {
                return "Hace " + diffInMins + " minuto"; 
            }
            else
            {
                return "Hace " + diffInMins + " minutos";
            }
        }
        else
        {
            if(diffInHours === 1)
            {
                return "Hace " + diffInHours + " hora";
            }
            else
            {
                return "Hace " + diffInHours + " horas";
            }
        }
    } else if (diffInDays < 31) {
        if (diffInDays === 1)
        {
            return "Hace " + diffInDays + " día";
        }
        else
        {
            return "Hace " + diffInDays + " días";
        }
    } else {
        return fechaTemp.format("MMMM [de] YYYY");
    }
}