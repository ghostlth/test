(function () {

    var dateObj = (function () {
        var _date = new Date();
        return{
            getDate : function () {
                return _date
            },
            setDate : function (date) {
                _date = date;
            }
        };
    })();



   function renderHtml() {
       var calendar = document.getElementById('calendar');
       var titleBox = document.createElement("div");
       var bodyBox = document.createElement("div");

       titleBox.className = 'calendar-title-box';
       titleBox.innerHTML = "<span class='prev-month' id='prevMonth'></span>"+
           "<span class='calendar-title' id='calendarTitle'></span>"+
           "<span class='next-month' id='nextMonth'></span>";
       calendar.appendChild(titleBox);

       bodyBox.className = 'calendar-body-box';
       var _headHtml = "<tr>"+
           "<th>日</th>"+
           "<th>一</th>"+
           "<th>二</th>"+
           "<th>三</th>"+
           "<th>四</th>"+
           "<th>五</th>"+
           "<th>六</th>"+
           "</tr>"
       var _bodyHtml = "";

       for(var i = 0;i<6;i++){
           _bodyHtml += "<tr>"+
               "<td></td>"+
               "<td></td>"+
               "<td></td>"+
               "<td></td>"+
               "<td></td>"+
               "<td></td>"+
               "<td></td>"+
               "</tr>";
       }
       bodyBox.innerHTML = "<table id='calenderTable' class='calendar-table'>"+_headHtml+_bodyHtml+"</table>";

       calendar.appendChild(bodyBox);

   }

   function showCalendarData() {
       var _year = dateObj.getDate().getFullYear();
       var _month = dateObj.getDate().getMonth()+1;
       var _dateStr = getDateStr(dateObj.getDate());

       var calendarTitle = document.getElementById('calendarTitle');
       var titleStr = _dateStr.substr(0,4)+"年"+_dateStr.substr(4,2)+"月";
       calendarTitle.innerText = titleStr;

       var _table = document.getElementById("calenderTable");
       var _tds = _table.getElementsByTagName("td");
       var _firstDay = new Date(_year,_month-1,1);
       for (var i = 0; i<_tds.length;i++){
           var _thisDay = new Date(_year,_month-1,i+1-_firstDay.getDay());

           var _thisDayStr = getDateStr(_thisDay);
           _tds[i].innerText = _thisDay.getDate();
           _tds[i].setAttribute('name',_thisDayStr);
           if(_thisDayStr ==getDateStr(new Date())){
               _tds[i].className = 'currentDay';
           }else if(_thisDayStr.substr(0,6)==getDateStr(new Date()).substr(0,6)){
               _tds[i].className = 'currentMonth';
           }else {
               _tds[i].className = 'otherMonth';
           }
       }
       getImpDate();
   }

   function bindEvent() {
       var prevMonth = document.getElementById('prevMonth');
       var nextMonth = document.getElementById('nextMonth');
       var calendarTitle = document.getElementById('calendarTitle');
       prevMonth.addEventListener('click',toPrevMonth);
       nextMonth.addEventListener('click',toNextMonth);
       calendarTitle.addEventListener('click',function () {
           dateObj.setDate(new Date());
           showCalendarData();
       });
   }
    
   function toPrevMonth() {
       var date = dateObj.getDate();
       dateObj.setDate(new Date(date.getFullYear(),date.getMonth()-1,1));
       showCalendarData();
   }

   function toNextMonth() {
       var date = dateObj.getDate();
       dateObj.setDate(new Date(date.getFullYear(),date.getMonth()+1,1));
       showCalendarData();
   }

    function getDateStr(date) {
        var _year = date.getFullYear();
        var _month = date.getMonth()+1;
        var _d = date.getDate();
        _month = (_month>9) ? String(_month) : ("0"+_month);
        _d = (_d>9) ? String(_d) :("0"+_d);
        return _year+_month+_d
    }

    //设置特殊日期
    function getImpDate() {
        var _impDate = document.getElementsByName('importDate');
        for (var i =0;i<_impDate.length;i++){
            var date =_impDate[i].value.split('|')[0];
            var msg = _impDate[i].value.split('|')[1];
            setAlert(date,msg);
            // console.log(_impDate[i]);
        }
    }

    function setAlert(date,msg) {
        var _dateCell = document.getElementsByName(date)[0];
        if(_dateCell){
            _dateCell.className = 'importDate';
            _dateCell.setAttribute('title',msg);
        }else {
            return
        }
    }

    renderHtml();
    showCalendarData();
    bindEvent();

})();