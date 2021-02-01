function rafraichir() {
    var text = '';
    var date = new Date();
    var jour_actuel = date.getDay();
    var chaine_jour = Array('Dimanche', 'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi');
    var jour_semaine = chaine_jour[jour_actuel];
    if (date.getDate() <= 9) {
        var jour = '0' + date.getDate();
    } else {
        var jour = date.getDate();
    }
    var mois_actuel = date.getMonth();
    var chaine_mois = Array('janvier', 'f&eacute;vrier', 'mars', 'avril', 'mai', 'juin',
        'juillet', 'ao&ucirc;t', 'septembre', 'octobre', 'novembre', 'd&eacute;cembre');
    var mois = chaine_mois[mois_actuel];

    if (date.getHours() <= 9) {
        var heure = '0' + date.getHours();
    } else {
        var heure = date.getHours();
    }

    if (date.getMinutes() <= 9) {
        var minutes = '0' + date.getMinutes();
    } else {
        var minutes = date.getMinutes();
    }
    if (date.getSeconds() <= 9) {
        var secondes = '0' + date.getSeconds();
    } else {
        var secondes = date.getSeconds();
    }
    text += jour_semaine + ' ' + jour + ' ' + mois + ' ' + date.getFullYear() + ' - ' + heure + ' : ' + minutes + ' : ' + secondes;
    document.getElementById('affiche_date').innerHTML = text;
}
setInterval('rafraichir()', 1000);
