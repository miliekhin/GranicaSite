export class util {
    static formatDigitSpaceSeparated( digit ){
        if( !digit ){
            return '';
        }
        if( typeof(digit) === "string" ){
            digit = Number(digit);
        }
        let d_str = digit.toLocaleString();
        return d_str.replace(',', '.');
    };

    static isDeclarationFilled( inputsData ){
        for(let itm of inputsData){
            let val = localStorage.getItem(itm.localStorageKey);
            if ( val !== null ){
                // console.log('isDeclarationFilled', val)
                return true;
            }
        }
        return false;
    }

    static dateDiffInDays(a, b){
        // a and b are javascript Date objects
        // Discard the time and time-zone information.
        const utc1 = Date.UTC(a.getFullYear(), a.getMonth(), a.getDate());
        const utc2 = Date.UTC(b.getFullYear(), b.getMonth(), b.getDate());
        return Math.floor((utc2 - utc1) / 86400000);
    }

    static textDateTime(added){
        let date_obj = {}
        if(!added) {
            date_obj.date = 'Сегодня'
            date_obj.time = '00:00'
            return date_obj
        }
        let options = { year: '2-digit', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit' };
        let addd = new Date(added)

        let now = new Date()
        // console.log(added.getHours())
        let days_diff = this.dateDiffInDays(addd, now)
        let date_str = addd.toLocaleString('ru-RU', options)
        date_obj.date = date_str.substr(0, 8)
        date_obj.time = date_str.substr(-5)
        date_str.replace(',', '')
        if(!days_diff)
            date_obj.date = 'Сегодня'
        if(days_diff === 1)
            date_obj.date = 'Вчера'

        // date_obj.time += Math.floor(Math.random() * 22)
        return date_obj
    }
}