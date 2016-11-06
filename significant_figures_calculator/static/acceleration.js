function print_num_html(num_object)
{
    numbertemp = String(num_object.number);
    number = numbertemp.slice(0, numbertemp.length - num_object.point_len) + "." + numbertemp.slice(numbertemp.length - num_object.point_len, numbertemp.length);
    if(String(num_object.number).length <= num_object.estimated)
    {
        return "<ins class='color'>" + number + "</ins>";
    }
    if(num_object.estimated <= num_object.point_len)  //估計值在小數點後
    {
        var ret = number.slice(0, number.length - num_object.estimated);
        ret = ret + "<ins class='color'>";
        ret = ret + number.slice(number.length - num_object.estimated, number.length);
        ret = ret + "</ins>";
        return ret;
    }
    else
    {
        var ret = number.slice(0, number.length - num_object.estimated - 1);
        ret = ret + "<ins class='color'>";
        ret = ret + number.slice(number.length - num_object.estimated - 1, number.length);
        ret = ret + "</ins>";
        return ret;
    }
}
