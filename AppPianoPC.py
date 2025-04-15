# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import datetime # Necessario per i timestamp delle note

# --- Definizione Struttura Dati PEC Senigallia ---
# (Uso la struttura dati popolata nella risposta precedente, la ometto qui per brevità)
# Assicurati che la variabile 'pec_data' sia definita qui come nel codice precedente.

# <------------------------------------------------------>
# <---- INCOLLA QUI LA STRUTTURA DATI pec_data COMPLETA --->
# <------------------------------------------------------>
pec_data = {
    # === DATI DINAMICI PER RISCHIO/FASE ===
    "Idrogeologico - Idraulico": { # Cap. F
        "Fase di Attenzione": { # F.4 - pag. 72 / Tabella pag. 73-75
            "Sindaco": [
                "Sentito il Gruppo ristretto, che è formato dalla F1, F7 e F11, dispone l’apertura del COC con le Funzioni di supporto necessarie e della SOC;", # pag. 73
                "segue l’evoluzione dell’evento tramite il collegamento con la SOUP e le informazioni che riceve da Gruppo Ristretto con il quale si coordina e confronta per decidere gli eventuali passaggi di Fase;", # pag. 73
                "dispone l’avviso alla popolazione." # pag. 73
            ],
            "Funzione 1": [ # Tecnico scientifica e pianificazione
                "Aggiorna costantemente lo scenario di rischio in base alle informazioni ricevute dalle Funzioni attive, dalla SOC e dal CFMR;", # pag. 73
                "dispone le attività di monitoraggio del territorio;", # pag. 73
                "propone le varie soluzioni tecniche atte a contenere l’evoluzione negativa dell'evento;", # pag. 74
                "gestisce la segreteria del COC (modalità di funzionamento, moduli verbali riunioni, rilievo presenze)." # pag. 74
            ],
            "Funzione 2": [ # Sanità e Veterinaria
                "Contatta le strutture sanitarie individuate in fase di pianificazione, comprese le farmacie, ne verifica la disponibilità;", # pag. 74
                "si predispone ad avvisare ed informare la popolazione da loro assistita, con l’ausilio della C.R.I." # pag. 74
            ],
            "Funzione 3": [ # Volontariato
                "Dispone l’apertura del Centro operativo Volontari CV;", # pag. 74
                "attiva tutte le associazioni di volontariato di Protezione Civile che operano nel territorio;", # pag. 74
                "dispone la partecipazione dei volontari all’attività di monitoraggio del territorio;", # pag. 74
                "richiede al Coordinatore del Gruppo Comunale, in contatto con tutte le associazioni di volontariato, la formazione delle squadre dei Volontari di Protezione Civile;" # pag. 74
            ],
            "Funzione 4": [ # Materiali, mezzi e squadre operative comunali
                "Attiva la squadra degli operai dell’area tecnica reperibile;", # pag. 74
                "esegue il monitoraggio del territorio con l’ausilio delle altre Funzioni di supporto;", # pag. 74
                "comunica la Fase di attenzione alle Ditte di supporto." # pag. 74
            ],
            "Funzione 5": [ # Servizi essenziali, edifici e impianti pubblici
                "Posizionamento in attesa (vedi pag. 75)." # Adattato da descrizione generale funzioni in attesa
            ],
            "Funzione 6": [ # Censimento danni a persone e cose
                 "Posizionamento in attesa (vedi pag. 75)."
            ],
            "Funzione 7": [ # Strutture operative locali e Viabilità
                "Indirizza le squadre di Polizia Locale in servizio sul territorio;", # pag. 74
                "allerta i reperibili." # pag. 74
            ],
             "Funzione 8": [ # Telecomunicazioni e Sistemi Informativi
                 "Posizionamento in attesa (vedi pag. 75)."
            ],
            "Funzione 9": [ # Matrici Ambientali
                "Attiva i dipendenti a disposizione dell’Area Ambiente e Porto per controllare lo stato degli scarichi a mare;", # pag. 74
                "allerta la Ditta appaltatrice della pulizia delle spiagge." # pag. 74
            ],
            "Funzione 10": [ # Assistenza alla popolazione
                 "Redige l’elenco delle strutture sensibili aperte di competenza, le contatta;", # pag. 74
                 "si coordina con la Funzione 2 e con la C.R.I. per avvisare ed informare la popolazione da loro assistita." # pag. 75
            ],
            "Funzione 11": [ # Comunicazione e attività scolastica
                "Avvisa i Dirigenti scolastici dei quattro Istituti Comprensivi;", # pag. 75
                "redige comunicati stampa rivolti ai quotidiani, giornali on-line e radio locali;", # pag. 75
                "aggiorna i siti www.comune.senigallia.an.it e www.protezionecivilesenigallia.it e la pagina Facebook “Comune di Senigallia”;", # pag. 75
                "invia SMS con il sistema di messaggistica predisposto." # pag. 75
            ],
            "Funzione 12": [ # Economica e Amministrativa
                 "Posizionamento in attesa (vedi pag. 75)."
            ]
        },
        "Fase di Preallarme": { # F.5 - pag. 75 / Tabella pag. 76-78
            "Sindaco": [
                "Nel caso non sia già stata attivata la Fase di attenzione: sentito il Gruppo ristretto, che è formato dalla F1, F7, F11, dispone l’apertura del COC con le Funzioni di supporto necessarie e della SOC;", # pag. 76
                "dispone l’avviso alla popolazione." # pag. 76
            ],
            "Funzione 1": [
                "Aggiorna costantemente lo scenario di rischio in base alle informazioni ricevute dalle Funzioni attive, dalla SOC e dal CFMR;", # pag. 76
                "coordina il monitoraggio del territorio tramite le squadre di tecnici, volontari e Polizia Locale;", # pag. 76
                "ipotizza l'ampiezza delle zone a rischio;", # pag. 76
                "coordina gli avvisi alla popolazione;", # pag. 76
                "propone le varie soluzioni tecniche atte a contenere l’evoluzione negativa dell'evento;", # pag. 76
                "dispone che i responsabili di funzione emettano, se lo ritengono necessario, l’ordine di servizio di reperibilità per il personale;", # pag. 76
                "gestisce la segreteria del COC (modalità di funzionamento, moduli verbali riunioni, rilievo presenze)." # pag. 76
            ],
            "Funzione 2": [
                "Contatta le strutture sanitarie individuate in fase di pianificazione, comprese le farmacie, ne verifica la disponibilità;", # pag. 76
                "attiva ed organizza il servizio sanitario ovvero verifica la disponibilità dei posti letto liberi nelle strutture sanitarie sicure;", # pag. 76
                "avvisa la popolazione da loro assistita, con l’ausilio della C.R.I. della Fase di preallarme;", # pag. 76
                "attiva il Servizio Veterinario dell’ASUR per il censimento del patrimonio zootecnico minacciato dall’evento e per la predisposizione di quanto necessario per la sua messa in sicurezza." # pag. 76
            ],
            "Funzione 3": [
                "Se non lo è già dispone l’apertura del Centro operativo Volontari CV;", # pag. 76
                "attiva tutte le associazioni di volontariato di Protezione Civile che operano nel territorio o le avvisa dei cambiamenti di Fase;", # pag. 76
                "richiede al Coordinatore del Gruppo Comunale in contatto con tutte le associazioni di volontariato attive nel territorio comunale, la formazione delle squadre dei Volontari di Protezione Civile per il monitoraggio del territorio in collaborazione con le altre Funzioni preposte;", # pag. 77
                "dispone la diffusione delle comunicazioni alla popolazione da parte dei Volontari di Protezione Civile in collaborazione con le altre Funzioni preposte." # pag. 77
            ],
            "Funzione 4": [
                "Attiva la squadra degli operai dell’area tecnica reperibile;", # pag. 77
                "partecipa al monitoraggio del territorio;", # pag. 77
                "comunica la Fase di preallarme alle Ditte di supporto;", # pag. 77
                "se necessarie attiva del Ditte di supporto." # pag. 77
            ],
            "Funzione 5": [
                "Avvisa i gestori delle reti luce, acqua e gas della attivazione della Fase di preallarme." # pag. 77
            ],
             "Funzione 6": [ # Censimento danni a persone e cose
                "Posizionamento in stand-by (vedi pag. 78)." # Funzioni 5, 6 vengono informate e restano in stand-by
            ],
            "Funzione 7": [
                "Richiama in servizio il personale di Polizia Locale che ritiene opportuno;", # pag. 77
                "controlla la viabilità principale coinvolta;", # pag. 77
                "diffonde le comunicazioni alla popolazione in collaborazione con le altre Funzioni preposte." # pag. 77
            ],
            "Funzione 8": [
                "Avvisa gli Enti Gestori dei servizi di telecomunicazione e informativi della Fase di preallarme." # pag. 77
            ],
            "Funzione 9": [
                "Attiva i dipendenti a disposizione dell’Area Ambiente e Porto per controllare lo stato degli scarichi a mare;", # pag. 77
                "attiva la Ditta appaltatrice della pulizia delle spiagge per garantire il corretto funzionamento degli scarichi a mare dei fossi." # pag. 77
            ],
            "Funzione 10": [
                "Redige l’elenco delle strutture sensibili aperte di competenza, le contatta;", # pag. 77
                "si coordina con la Funzione 2 e con la C.R.I. per avvisare ed informare la popolazione da loro assistita." # pag. 77
            ],
            "Funzione 11": [
                "Avvisa i Dirigenti scolastici dei 4 Istituti Comprensivi l’attivazione della Fase in atto;", # pag. 78
                "informa la popolazione dell’attivazione della Fase di in atto tramite: Uffici Comunicazione, comunicati stampa rivolti ai quotidiani, giornali on-line e radio locali;", # pag. 78
                "aggiorna i siti www.comune.senigallia.an.it e www.protezionecivilesenigallia.it la pagina Facebook “Comune di Senigallia”;", # pag. 78
                "invia SMS con il sistema di messaggistica predisposto;", # pag. 78
                "collabora alla predisposizione dei messaggi da diffondere alla popolazione da parte delle Funzioni preposte." # pag. 78
            ],
             "Funzione 12": [ # Economica e Amministrativa
                 "Partecipa alla seduta del COC e rimane a disposizione per quanto di competenza." # pag. 78
             ]
        },
        "Fase di Allarme": { # F.6 - pag. 78 / Tabella pag. 79-84
             "Sindaco": [
                "A seguito dell’emissione di una Allerta Arancione o Rossa o per il superamento delle soglie di allarme idro pluviometriche sentito il Gruppo ristretto, che è formato dalla F1, F7, F11 o le Funzioni di supporto attive se il COC è già aperto: dispone il passaggio alla Fase di allarme;", # pag. 79
                "se non già aperto dispone l’apertura del COC con tutte le Funzioni di supporto e della SOC;", # pag. 79
                "dispone le comunicazioni alla popolazione.", # pag. 79
                "[Evacuazione] Emana le Ordinanze di Evacuazione sentito il COC." # pag. 79
            ],
            "Funzione 1": [
                "Gestisce l’evoluzione dell’evento coordinando tutte le Funzioni di supporto che operano secondo le proprie mansioni, in particolare: aggiorna costantemente lo scenario di rischio in base alle informazioni ricevute dalle Funzioni di supporto, dalla SOC e dal CFMR,", # pag. 80
                "coordina il monitoraggio del territorio tramite le squadre di tecnici, volontari e Polizia Locale,", # pag. 80
                "aggiorna la valutazione dell'ampiezza delle zone a rischio,", # pag. 80
                "coordina l’attività di avviso alla popolazione,", # pag. 80
                "propone le varie soluzioni tecniche atte al contenimento del danno,", # pag. 80
                "dispone, se necessario, la verifica dell’agibilità delle aree d’emergenza,", # pag. 80
                "gestisce la segreteria del COC (modalità di funzionamento, moduli verbali riunioni, schede di rilievo criticità, rilievo presenze);", # pag. 80
                "dispone il richiamo in servizio del personale comunale.", # pag. 80
                "[Evacuazione] Coordina le Funzioni di supporto per: l’attività di evacuazione, l‘avviso di evacuazione alla popolazione; il supporto alla popolazione recatasi presso le aree di attesa; l’apertura dei centri di accoglienza ritenuti necessari in considerazione dell’evoluzione dell’evento." # pag. 80
            ],
             "Funzione 2": [
                "Verifica la disponibilità delle associazioni di volontariato individuate in fase di pianificazione, per il trasporto e l’assistenza alla popolazione presente nelle strutture sanitarie e nelle abitazioni in cui vi sono malati gravi o disabili;", # pag. 80
                "verifica la disponibilità dei posti letto liberi nelle strutture sanitarie sicure;", # pag. 80
                "comunica agli assistiti a domicilio la Fase di allarme;", # pag. 80
                "organizza le attività di evacuazione degli assistiti in collaborazione con la C.R.I.;", # pag. 80
                "[Evacuazione] se necessario attiva l’evacuazione di alcuni assistiti in particolare difficoltà in collaborazione con la C.R.I. e le associazioni di volontariato;", # pag. 80
                "allarma il Servizio Veterinario dell’ASUR affinché provveda: all’alimentazione degli animali, in caso di necessità, al trasferimento degli animali in idonee strutture (stalle)." # pag. 80
                "[Evacuazione] Comunica agli assistiti a domicilio dell’emissione dell’ordinanza di evacuazione;", # pag. 81
                "[Evacuazione] attiva l’evacuazione degli assistiti non ancora messi in sicurezza in collaborazione con la C.R.I. e le associazioni di volontariato;", # pag. 81
                "[Evacuazione] crea eventuali cordoni sanitari con Posti Medici Avanzati (PMA);", # pag. 81
                "[Evacuazione] attiva il Servizio Veterinario della ASUR per la messa in sicurezza del patrimonio zootecnico e provveda alla raccolta di carcasse in aree idonee ed esegue operazioni residuali collegate all’evento." # pag. 81
            ],
            "Funzione 3": [
                "Se non è già aperto dispone l’immediata apertura del CV;", # pag. 81
                "attiva tutte le associazioni di volontariato di Protezione Civile che operano nel territorio o le avvisa dei cambiamenti di Fase;", # pag. 81
                "richiede al Coordinatore del Gruppo Comunale, in contatto con tutte le associazioni di volontariato attive nel territorio comunale, la formazione delle squadre di PC secondo le specifiche attitudini e la determinazione delle turnazioni;", # pag. 81
                "coordina le attività del Volontariato con le altre Funzioni alle quali da supporto, in particolare: per il monitoraggio del territorio in particolare presidia i punti critici ed effettua il controllo visivo della situazione dei fossi e della viabilità, per la diffusione delle comunicazioni alla popolazione, con la Funzione 4 per la verifica, se necessaria, dell’agibilità delle aree di attesa, con le Forze dell’Ordine nel presidiare i blocchi stradali disposti.", # pag. 81
                "[Evacuazione] Collabora con la Funzione 7 e 10 per il supporto alla popolazione recatasi presso le aree di attesa;", # pag. 81
                "[Evacuazione] Collabora con le altre Funzioni all’apertura dei centri di accoglienza ritenuti necessari rispetto all’evoluzione dell’evento." # pag. 81
            ],
            "Funzione 4": [
                 "Con la squadra attiva di operai dell’Area tecnica e con le eventuali Ditte di supporto, se attivate, ripristina l’agibilità delle aree di attesa se ritenute inagibili;", # pag. 81
                 "verifica la disponibilità, anche presso altre Enti Pubblici, di materiali, attrezzature e mezzi necessari ad assicurare l’assistenza alla popolazione presso i centri di accoglienza.", # pag. 81
                 "[Evacuazione] Predispone l’allestimento dei centri di accoglienza aperti (servizi essenziali);", # pag. 82
                 "[Evacuazione] disloca i materiali, attrezzature e mezzi necessari ad assicurare l’assistenza alla popolazione presso i centri di accoglienza;", # pag. 82
                 "[Evacuazione] coordina la sistemazione presso le aree di accoglienza dei materiali forniti da altri Enti Pubblici e gestisce il flusso di carico e scarico di materiali e mezzi;", # pag. 82
                 "[Evacuazione] è preposta all’approvvigionamento ed alla distribuzione di alimenti, generi di conforto e carburanti secondo le istruzioni ricevute." # pag. 82
            ],
            "Funzione 5": [
                "Prepara le strutture pubbliche per l’utilizzo e ne verifica l’efficienza, la ripristina se necessario;", # pag. 82
                "coordina con i gestori dei servizi luce, acqua e gas il monitoraggio e l’eventuale ripristino dei servizi stessi.", # pag. 82
                "[Evacuazione] Presiede al funzionamento degli impianti dei centri di accoglienza aperti e ne garantisce il funzionamento;", # pag. 82
                "[Evacuazione] si adopera per il ripristino dei servizi essenziali, ricorrendo anche a fonti di approvvigionamento alternative." # pag. 82
            ],
            "Funzione 6": [
                "Partecipa alle riunioni del COC e rimane a disposizione per quanto di competenza;", # pag. 82
                "ottenuto il quadro sommario della situazione, se necessario, si coordina con il referente della Funzione 1 per predisporre le ordinanze di evacuazione e di sgombero dei fabbricati gravemente danneggiati ed eventualmente degli Istituti scolastici." # pag. 82
            ],
            "Funzione 7": [
                "Richiama in servizio tutto il personale di Polizia Locale disponibile se non già richiamato;", # pag. 82
                "dispone ed esegue i blocchi stradali con materiale fornito dalla Funzione 4;", # pag. 82
                "controlla la viabilità coinvolta in collaborazione con le Forze dell’Ordine;", # pag. 82
                "partecipa alla diffusione delle comunicazioni alla popolazione.", # pag. 82
                "[Evacuazione] Partecipa alla diffusione degli ordini di Evacuazione;", # pag. 83
                "[Evacuazione] Collabora con le Funzione 3 e 10 per il supporto alla popolazione recatasi presso le aree di attesa;", # pag. 83
                "[Evacuazione] Collabora con le altre Funzioni all’apertura dei centri di accoglienza ritenuti necessari rispetto all’evoluzione dell’evento", # pag. 83
                "[Evacuazione] concorre con le forze dell’ordine presenti sul territorio ad attività di pattugliamento delle aree evacuate, prevenendo azioni di sciacallaggio." # pag. 83
            ],
             "Funzione 8": [
                "Controlla e garantisce l’efficienza per quanto di competenza dei sistemi di telecomunicazione e informativi per l’affidabilità dei servizi informativi;", # pag. 83
                "attiva il contatto con gli Enti Gestori dei servizi di telecomunicazione e informativi." # pag. 83
            ],
            "Funzione 9": [
                "Attiva la Ditta appaltatrice della pulizia delle spiagge per garantire il corretto funzionamento degli scarichi a mare dei fossi.", # pag. 83
                "[Evacuazione] Garantisce i servizi sanitari primari (pulizia degli spazi comuni, servizi igienici e raccolta rifiuti) nelle aree di attesa, centri di accoglienza;", # pag. 83
                "[Evacuazione] attiva le Ditte di supporto preventivamente individuate per assicurare gli interventi;", # pag. 83
                "[Evacuazione] organizza la raccolta e lo smaltimento delle macerie e dei rifiuti prodotti dall’evento calamitoso." # pag. 83
            ],
            "Funzione 10": [
                "Redige l’elenco delle strutture sensibili di propria competenza aperte e le tiene informate, le avvisa in caso di evacuazione;", # pag. 83
                "si coordina con la Funzione 2 e con la C.R.I. per tenere aggiornata la popolazione da loro assistita.", # pag. 83
                "[Evacuazione] Avvisa, coordinandosi con la Funzione 2 e con la C.R.I., la popolazione da loro assistita dell’emanazione dell’Ordinanza di evacuazione;", # pag. 84
                "[Evacuazione] si attiva per l’evacuazione e la messa in sicurezza degli assistiti e della popolazione in genere nelle aree di attesa e nei centri di accoglienza, in collaborazione con la C.R.I.", # pag. 84
                "[Evacuazione] valuta se necessario e ne fa richiesta dell’aiuto all'Amministrazione Provinciale e alla Prefettura, per quanto di competenza, per l’impiego dei mezzi speciali delle Forze di Pubblica Sicurezza nel trasporto di ammalati gravi verso i luoghi di cura o per approvvigionamento di carburanti, alimenti e generi di conforto in località isolate;", # pag. 84
                "[Evacuazione] Collabora con le Funzione 3 e 7 per il supporto alla popolazione recatasi presso le aree di attesa;", # pag. 84
                "[Evacuazione] Collabora con le altre Funzioni all’apertura dei centri di accoglienza ritenuti necessari rispetto all’evoluzione dell’evento" # pag. 84
            ],
            "Funzione 11": [
                "Avvisa i Dirigenti scolastici dei 4 Istituti Comprensivi l’attivazione della Fase di allarme;", # pag. 84
                "informa la popolazione dell’attivazione della Fase di allarme tramite: Uffici Comunicazione, comunicati stampa rivolti ai quotidiani, giornali on-line e radio locali;", # pag. 84
                "aggiorna i siti www.comune.senigallia.an.it e www.protezionecivilesenigallia.it, e la pagina Facebook “Comune di Senigallia”;", # pag. 84
                "invia SMS con il sistema di messaggistica predisposto;", # pag. 84
                "collabora alla predisposizione dei messaggi da diffondere alla popolazione da parte delle Funzioni preposte.", # pag. 84
                "[Evacuazione] Avvisa i Dirigenti scolastici dei 4 Istituti Comprensivi dell’Ordine di evacuazione;", # pag. 84
                "[Evacuazione] informa la popolazione comunicando l’ordine di evacuazione tramite: Uffici Comunicazione, comunicati stampa rivolti ai quotidiani, giornali on-line e radio locali." # pag. 84
            ],
            "Funzione 12": [
                "Collabora all’interno del COC nella predisposizione della modulistica, delle ordinanze e del protocollo;", # pag. 84
                "coadiuva le altre Funzioni di supporto al fine di garantire la regolarità contabile e amministrativa degli atti correlati all’emergenza;", # pag. 85
                "provvede alla regolare tenuta del registro delle spese per la successiva predisposizione degli atti amministrativi di copertura finanziaria." # pag. 85
            ]
        },
        "Fase di Cessata Emergenza": { # F.7 - pag. 85 / Tabella pag. 85-87
            "Sindaco": [
                "Il Sindaco che segue l’evoluzione dell’evento, constatati: la fine della perturbazione metereologica, il rientro alla normalità del territorio dei fossi e della viabilità, l’abbassamento sotto i livelli di attenzione dei corsi d’acqua del Fiume Misa e del Fiume Cesano, dichiara la Cessazione dell’Emergenza per esaurimento del fenomeno e dispone il ritorno alla normalità del tempo ordinario;", # pag. 85
                "finite le attività necessarie per la Fase di cessata emergenza e dopo che il COC abbia svolto le seguenti mansioni ordina la chiusura del COC e della SOC." # pag. 85
            ],
            "Funzione 1": [
                "Coordina tutte le Funzioni di supporto che operano il ripristino della normalità secondo le proprie mansioni;", # pag. 85
                "coordina l’attività di diffusione dell’informazione di Cessata emergenza;", # pag. 85
                "coordina le attività di ripristino della circolazione stradale, dei servizi essenziali, luce gas acqua, verificando preliminarmente la potabilità dell’acqua, e l’attività di bonifica del territorio;", # pag. 85
                "organizza, anche in collaborazione con i Vigili del Fuoco, la verifica degli immobili e del territorio;", # pag. 85
                "avvia il censimento dei danni subiti dalle persone ed alle strutture;", # pag. 85
                "gestisce la segreteria del COC (modalità di funzionamento, moduli verbali riunioni, schede di rilievo criticità, rilievo presenze)." # pag. 85
            ],
             "Funzione 2": [
                "Avvisa i propri assistiti della Cessata emergenza;", # pag. 85
                "[Evacuazione] nel caso di Evacuazione, previa verifica di idoneità, dispone il rientro degli assistiti nelle proprie abitazione;", # pag. 86
                "dispone il rientro degli animali nei propri siti." # pag. 86
            ],
             "Funzione 3": [
                "Collabora con le altre Funzioni preposte alla diffusione dell’informazione di Cessata emergenza;", # pag. 86
                "[Evacuazione] nel caso di Evacuazione collabora al rientro della popolazione nelle proprie abitazioni." # pag. 86
            ],
            "Funzione 4": [
                "Esegue le attività che permettano il ripristino: della circolazione stradale, dei servizi essenziali, luce gas acqua,", # pag. 86
                "verifica l’attività di ripristino del territorio." # pag. 86
            ],
            "Funzione 5": [
                 "Collabora con i gestori dei servizi essenziali, luce acqua gas, per il ripristino della funzionalità degli impianti." # pag. 86
            ],
            "Funzione 6": [
                "Esegue in collaborazione con i VVF i sopralluoghi per verificare l’idoneità e l’entità dei danni degli edifici e del territorio;", # pag. 86
                "Censisce i danni subiti dalla persone, dagli edifici, impianti industriali, attività produttive, agricoltura e zootecnia, opere di interesse culturale o riguardanti i servizi essenziali." # pag. 86
            ],
             "Funzione 7": [
                "Diffonde l’informazione di Cessata emergenza;", # pag. 86
                "verificata la possibilità di normale circolazione;", # pag. 86
                "ripristina la viabilità." # pag. 86
            ],
             "Funzione 8": [
                 "Nessuna azione specifica indicata per questa fase." # Da verificare nel dettaglio PEC se necessario
            ],
             "Funzione 9": [
                "Provvede ove necessario: al ripristino del corretto deflusso delle acque negli scarichi a mare, alla rimozione dei detriti dalle spiagge;", # pag. 86
                "verifica la potabilità dell’acqua;", # pag. 86
                "esegue sopralluoghi nelle strutture potenzialmente rilevanti per l’ambiente al fine di verificare l’eventuale danneggiamento o fuoriuscita di sostanze nocive per l’ambiente;", # pag. 86
                "organizza la raccolta e lo smaltimento delle macerie e dei rifiuti prodotti dall’evento calamitoso." # pag. 86
            ],
            "Funzione 10": [
                "Avvisa i Centri e gli assistiti di propria competenza della Cessata emergenza;", # pag. 86
                "[Evacuazione] nel caso di Evacuazione, previa verifica di idoneità, dispone il rientro della popolazione e degli assistiti nelle proprie abitazioni." # pag. 87
            ],
            "Funzione 11": [
                "Avvisa i Dirigenti scolastici dei 4 Istituti Comprensivi;", # pag. 87
                "informa la popolazione della Cessata emergenza tramite: Uffici Comunicazione, comunicati stampa rivolti ai quotidiani, giornali on-line e radio locali;", # pag. 87
                "aggiorna il sito www.comune.senigallia.an.it e www.protezionecivilesenigallia.it, e la pagina Facebook “Comune di Senigallia”;", # pag. 87
                "invia SMS con il sistema di messaggistica predisposto;", # pag. 87
                "predispone il testo dei messaggi da diffondere alla popolazione da parte delle Funzioni preposte." # pag. 87
            ],
             "Funzione 12": [
                "Nessuna azione specifica indicata per questa fase." # Da verificare nel dettaglio PEC se necessario
            ]
        }
    },
    # ... (altri rischi come Sismico, Neve, etc. con la stessa struttura)...
    # --- SEZIONI STATICHE ---
    "Glossario": { # pag. 15-21
        "Aree di emergenza": "aree destinate, in caso di emergenza, ad uso di protezione civile.",
        "Aree di attesa": "luoghi di prima accoglienza per la popolazione immediatamente dopo l’evento ove la popolazione riceverà le prime informazioni.", # pag. 15
        "Aree di ammassamento dei soccorritori e delle risorse": "centri di raccolta di uomini e mezzi per il soccorso della popolazione.", # pag. 15
        "Centri di accoglienza": "luoghi in cui saranno istallati i primi insediamenti abitativi o le strutture in cui si potrà alloggiare la popolazione colpita, sono strutture coperte opportunamente attrezzate per ospitare in via provvisoria la popolazione assistita.", # pag. 15
        "Attivazioni in emergenza": "rappresentano le immediate predisposizioni che dovranno essere attivate dai centri operativi.", # pag. 15
        "Attività addestrativa": "la formazione degli operatori di protezione civile e della popolazione tramite corsi ed esercitazioni.", # pag. 15
        "Bonifica": "l'insieme degli interventi atti ad eliminare le fonti di inquinamento e le sostanze inquinanti o a ridurre le concentrazioni delle stesse...", # pag. 15
        "Calamità": "è un evento naturale o legato ad azioni umane, nel quale tutte le strutture fondamentali della società sono inagibili o distrutte su un ampio tratto del territorio; eventi che debbono essere fronteggiati con mezzi ed attività straordinarie.", # pag. 15
        "Catastrofe": "è un evento... provocato da cause naturali o da azioni umane, nel quale però le strutture fondamentali della società rimangono nella quasi totalità intatte, efficienti ed agibili.", # pag. 15
        "Centro Operativo": "è in emergenza l’organo di coordinamento delle strutture di protezione civile sul territorio colpito...", # pag. 15
        "DI.COMA.C.": "Direzione Comando e Controllo, esercita sul luogo dell’evento il coordinamento nazionale.", # pag. 15
        "C.C.S.": "Centro Coordinamento Soccorsi, gestisce gli interventi a livello provinciale...", # pag. 15
        "C.O.M.": "Centro Operativo Misto, operano sul territorio di più Comuni in supporto all’attività dei Sindaci.", # pag. 15
        "C.O.C.": "Centro Operativo Comunale, presieduto dal Sindaco, provvede alla direzione dei soccorsi e dell’assistenza della popolazione del comune.", # pag. 15
        "Centro Situazioni": "è il centro nazionale che raccoglie e valuta informazioni e notizie relative a qualsiasi evento...", # pag. 15
        "Commissario delegato": "è l’incaricato da parte del Consiglio dei Ministri per l’attuazione degli interventi di emergenza...", # pag. 16
        "Evento": "fenomeno di origine naturale o antropica in grado di arrecare danno alla popolazione...", # pag. 17
        "Fasi operative": "è l’insieme delle azioni di protezione civile centrali e periferiche da intraprendere prima (per i rischi prevedibili), durante e dopo l’evento...", # pag. 17
        "Funzioni di supporto": "sono l’organizzazione delle risposte, distinte per settori di attività e di intervento, che occorre dare alle diverse esigenze operative.", # pag. 17
    },
    "Acronimi": { # pag. 21-22
        "CAPI": "Centro Assistenziale di Pronto Intervento", # pag. 21
        "Cat": "Centro di allerta tsunami", # pag. 21
        "CCP": "Centro di Controllo Provinciale", # pag. 21
        "C.C.S.": "Centro Coordinamento Soccorsi", # pag. 21
        "CCSR": "Centro di Controllo e Supervisione Regionale", # pag. 21
        "CE.SI": "CEntro SItuazioni Protezione Civile", # pag. 21
        "CFMR": "Centro Funzionale Multirischi Regionale", # pag. 21
        "CGR": "Centro Gestione Rete", # pag. 21
        "COAU": "Centro Operativo Aereo Unificato", # pag. 21
        "C.O.C.": "Centro Operativo Comunale", # pag. 21
        "COEMM": "Centro Operativo Emergenze Marittime", # pag. 21
        "C.O.I.": "Centro Operativo Intercomunale", # pag. 21
        "C.O.M.": "Centro Operativo Misto", # pag. 21
        "COR": "Centro Operativo Regionale", # pag. 21
        "CV": "Centro operativo Volontari", # pag. 21
        "DB.Com.": "Banca Dati Comuni e Enti Sistema", # pag. 21
        "DI.COMA.C.": "DIrezione COMAndo e Controllo", # pag. 21
        "DSTN": "Dipartimento dei Servizi Tecnici Nazionali", # pag. 21
        "GIS": "Geographic Information System", # pag. 21
        "GNDCI": "Gruppo Nazionale per la Difesa delle Catastrofi Idrogeologiche", # pag. 21
        "INGV": "Istituto Nazionale di Geofisica e Vulcanologia", # pag. 21
        "P.A.I.": "Piano di Assetto Idrogeologico", # pag. 21
        "PMA": "Posto Medico Avanzato", # pag. 21
        "RESIICO": "REte SIsmometrica dell’Italia Centro Orientale", # pag. 21
        "RMIPR": "Rete Meteo Idro-Pluviometrica Regionale", # pag. 21
        "SiAM": "Sistema d’Allertamento nazionale per i Maremoti generati da sisma", # pag. 22
        "SOI": "Sala Operativa Integrata", # pag. 22
        "SOUP": "Sala Operativa Unificata Permanente", # pag. 22
        "SPCSL": "Sistema regionale di Protezione Civile e Sicurezza Locale", # pag. 22
        "ASUR": "Azienda Sanitaria Unica Regionale",
        "ARPA(M)": "Agenzia Regionale per la Protezione Ambientale (delle Marche)",
        "C.R.I.": "Croce Rossa Italiana",
        "LL.PP.": "Lavori Pubblici",
        "P.O.": "Posizione Organizzativa",
        "E.Q.": "Elevata Qualificazione (Incarico dirigenziale/funzionario)",
        "VV.F.": "Vigili del Fuoco",
        "UTG": "Ufficio Territoriale del Governo (Prefettura)",
        "D.O.S.": "Direttore Operazioni di Spegnimento (Incendi)",
        "AIB": "Antincendio Boschivo",
        "S.I.S.P.": "Servizio Igiene e Sanità Pubblica"
    },
    "FunzioniSupporto": { # pag. 40-41 Responsabili, pag. 42-57 Compiti
        "F1": {"Nome": "Tecnico scientifica e pianificazione", "Responsabile": "Responsabile PO Protezione Civile", "Info": "Coordinamento tecnico, valutazione scenari, monitoraggio, pianificazione emergenza, censimento danni, agibilità. (pag. 42-44)"},
        "F2": {"Nome": "Sanità e Veterinaria", "Responsabile": "Medico di igiene e sanità pubblica Area Vasta 2, Dipartimento Prevenzione...", "Info": "Assistenza sanitaria, gestione PMA, igiene pubblica, assistenza veterinaria, supporto persone fragili. (pag. 44-46)"},
        "F3": {"Nome": "Volontariato", "Responsabile": "Responsabile Sala Operativa Comunale di Protezione Civile", "Info": "Coordinamento gruppi volontariato, attivazione squadre, supporto logistico e operativo alle altre funzioni. (pag. 46-47)"},
        "F4": {"Nome": "Materiali, mezzi e squadre tecnico-operative", "Responsabile": "Responsabile PO Manutenzioni - LL.PP", "Info": "Gestione mezzi, materiali, attrezzature comunali e da reperire; coordinamento squadre operative. (pag. 47-48)"},
        "F5": {"Nome": "Servizi essenziali, edifici e impianti pubblici", "Responsabile": "Responsabile PO Manutenzioni - LL.PP", "Info": "Monitoraggio e ripristino reti (acqua, luce, gas, ecc.), agibilità edifici pubblici strategici. (pag. 48-50)"},
        "F6": {"Nome": "Censimento danni a persone e cose", "Responsabile": "Responsabile PO Area Tecnica Territorio ed Edilizia privata", "Info": "Verifica danni e agibilità edifici privati, immobili storico-monumentali, infrastrutture. (pag. 50-51)"},
        "F7": {"Nome": "Strutture operative locali e Viabilità", "Responsabile": "Comandante della Polizia Locale", "Info": "Gestione viabilità, chiusura strade, percorsi alternativi, presidio varchi, coordinamento forze ordine. (pag. 51-52)"},
        "F8": {"Nome": "Telecomunicazioni e Sistemi Informativi", "Responsabile": "Responsabile PO Sistemi informatici", "Info": "Mantenimento funzionalità sistemi TLC e informatici, gestione comunicazioni emergenza. (pag. 52-53)"},
        "F9": {"Nome": "Matrici Ambientali", "Responsabile": "Responsabile PO Ambiente, Porto, Demanio marittimo, Verde pubblico", "Info": "Monitoraggio e tutela matrici ambientali (aria, acqua, suolo), gestione rifiuti emergenza. (pag. 53)"},
        "F10": {"Nome": "Assistenza alla popolazione", "Responsabile": "Dirigente Area Servizi Sociali e Ambito Territoriale Sociale n. 8...", "Info": "Gestione aree accoglienza, censimento sfollati, distribuzione beni necessità, supporto persone fragili. (pag. 54-55)"},
        "F11": {"Nome": "Comunicazione e attività scolastica", "Responsabile": "Responsabile PO Affari generali - Comunicazione - Turismo/Eventi e Sviluppo economico", "Info": "Informazione a popolazione e media, gestione comunicati, rapporti con scuole. (pag. 55-56)"},
        "F12": {"Nome": "Economica e Amministrativa", "Responsabile": "Responsabile PO Finanze, Tributi, Economato", "Info": "Gestione risorse finanziarie emergenza, procedure spesa, rendicontazione. (pag. 56-57)"},
    },
    "AreeEmergenza": { # E.2 - pag. 58-62
        "Descrizioni": {
            "Aree di Attesa": "luoghi dove confluirà la popolazione a rischio in caso di allarme, emergenza ed evacuazione; luoghi di prima accoglienza.", # pag. 58
            "Centri di Accoglienza": "luoghi sicuri dove esistono già strutture coperte o dove saranno allestite le tende e i moduli abitativi temporanei per ospitare... la popolazione proveniente dalle aree di attesa.", # pag. 58, 60
            "Aree di Ammassamento Soccorritori": "spazi scoperti ubicati in luogo sicuro per ospitare i soccorritori del sistema di protezione civile, i loro mezzi, le loro attrezzature e le loro strutture.", # pag. 58, 61
            "Zone di Atterraggio": "spazi scoperti e liberi da ostacoli per l’avvicinamento e di adeguate dimensioni per l’atterraggio di elicotteri.", # pag. 58, 62 (Piazzale Stadio Bianchelli)
        },
        "Cancelli": "Posti di blocco istituiti per regolamentare la circolazione in entrata e in uscita sul perimetro delle zone a rischio molto elevato/elevato, con l’ausilio dei volontari di Protezione Civile nei cancelli meno problematici. (Vedere E.3.2, pag. 62 e Allegato 10 PEC)", # pag. 62
        "ElenchiSpecifici": [
            "Nota: Gli elenchi specifici delle Aree di Attesa, Centri di Accoglienza, Aree Ammassamento, Zone Atterraggio e Cancelli sono dettagliati negli Allegati al Piano di Emergenza Comunale (es. F6, F7, F8, F9, F10, G5, G6, G7)." # Rif. Allegati F (pag. 98), G (pag. 118), ecc.
        ]
    },
    "NormeComportamento": {
        # ... (Norme di comportamento come nella risposta precedente) ...
        "Idrogeologico - Idraulico": [ # F.11 pag. 96 -> Pieghevole "Io non rischio alluvione" pag. 92
            "**COSA FARE PRIMA:**\n* Informati sul rischio idrogeologico della tua zona e sui piani di emergenza comunali.\n* Identifica le aree sicure più vicine e i percorsi per raggiungerle.\n* Prepara un kit di emergenza (acqua, cibo, medicinali, torcia, radio a pile, documenti).\n* Assicura oggetti mobili all'esterno che potrebbero essere trascinati dall'acqua.",
            "**DURANTE L'ALLERTA/PREALLARME:**\n* Segui gli aggiornamenti forniti dalle autorità (radio, TV, sito Comune, App FlagMii).\n* Non sostare su ponti, argini, rive di fiumi o torrenti.\n* Metti al sicuro beni e documenti importanti ai piani alti.\n* Se abiti in zona a rischio, preparati a una possibile evacuazione.",
            "**DURANTE L'ALLARME/EVENTO (SE SEI IN CASA):**\n* Non scendere in cantine, seminterrati o garage.\n* Se sei ai piani bassi, sali ai piani superiori. Evita l'ascensore.\n* Chiudi gas, luce e acqua se possibile e se non comporta rischi.\n* Non uscire se non strettamente necessario o ordinato dalle autorità.",
            "**DURANTE L'ALLARME/EVENTO (SE SEI FUORI CASA):**\n* Allontanati dalla zona allagata e raggiungi luoghi elevati e sicuri.\n* Non usare l'automobile, potrebbe essere trascinata via.\n* Non attraversare sottopassi, ponti o strade allagate.\n* Fai attenzione a possibili frane o smottamenti.",
            "**DOPO L'EVENTO:**\n* Segui le indicazioni delle autorità prima di muoverti o rientrare in casa.\n* Non toccare cavi elettrici caduti.\n* Non bere acqua dal rubinetto finché non dichiarata potabile.\n* Aiuta i vicini in difficoltà, se puoi farlo in sicurezza."
        ],
         "Sismico": [ # G.5 pag. 116 -> Pieghevole pag. 117
            "**COSA FARE PRIMA:**\n* Informati sulla classificazione sismica del tuo Comune e sulle norme costruttive.\n* Verifica la sicurezza della tua casa. Fissa alle pareti mobili alti/pesanti, scaffali, quadri.\n* Individua i punti sicuri in casa (sotto tavoli robusti, vani di porte in muri portanti, angoli tra pareti).\n* Tieni a portata di mano un kit di emergenza.\n* Impara a chiudere i rubinetti generali di acqua, gas e l'interruttore della luce.",
            "**DURANTE LA SCOSSA (SE SEI ALL'INTERNO):**\n* Mantieni la calma. Cerca riparo nel punto sicuro più vicino.\n* Non precipitarti fuori. Le scale potrebbero essere danneggiate e all'esterno potrebbero cadere oggetti.\n* Stai lontano da finestre, vetri, specchi e oggetti pesanti che potrebbero cadere.\n* Se sei a letto, rimani lì e proteggiti la testa con un cuscino.",
            "**DURANTE LA SCOSSA (SE SEI ALL'APERTO):**\n* Allontanati da edifici, alberi, linee elettriche, ponti, cavalcavia.\n* Cerca uno spazio aperto e attendi la fine della scossa.\n* Se sei in auto, fermati in un luogo sicuro lontano da pericoli e resta in auto.",
            "**DOPO LA SCOSSA:**\n* Verifica il tuo stato di salute e quello degli altri.\n* Esci dall'edificio con cautela, indossando scarpe robuste. Attento alle scale danneggiate.\n* Non usare l'ascensore.\n* Raggiungi le Aree di Attesa indicate dal Piano Comunale, senza usare l'auto se non necessario.\n* Non intralciare i mezzi di soccorso.\n* Limita l'uso del telefono per non sovraccaricare le linee.\n* Segui le informazioni fornite dalle autorità."
        ],
         "Neve": [ # H.4 pag. 129 -> Pieghevole pag. 130-131
            "**PRIMA:**\n* Informati sull'evoluzione meteo.\n* Procura attrezzatura necessaria (pala, scorte sale).\n* Verifica la tua auto (pneumatici invernali/catene, antigelo, tergicristalli, batteria).\n* Fai scorta di cibo, acqua, medicinali.\n* Proteggi i contatori dell'acqua.",
            "**DURANTE:**\n* Limita gli spostamenti.\n* Non utilizzare mezzi a due ruote.\n* Libera l'ingresso di casa dalla neve senza buttarla in strada.\n* Se usi stufe/camini, attenzione alla ventilazione.\n* Se costretto a usare l'auto: viaggia con cautela, mantieni distanze, evita manovre brusche, usa luci anabbaglianti.",
            "**DOPO:**\n* Attenzione al ghiaccio, anche dopo la rimozione della neve.\n* Rimuovi neve/ghiaccio da tetti/balconi.\n* Spostati a piedi con scarpe antiscivolo.",
        ],
         "Incendi Boschivi e d’Interfaccia": [ # I.9 pag. 146 -> Pieghevole pag. 147
            "**COSA FARE PRIMA:**\n* Non accendere fuochi.\n* Non gettare mozziconi.\n* Non parcheggiare su erba secca.\n* Pulisci l'area intorno a casa.\n* Tieni attrezzatura per spegnere piccoli focolai.",
            "**COSA FARE DURANTE:**\n* Chiama 115, 112 o 1515.\n* Allontanati dal fuoco.\n* Se l'incendio è vicino a casa: chiudi porte/finestre, sigilla fessure, allontana materiali infiammabili, bagna l'area intorno.\n* Abbandona la casa se ordinato.\n* Se sorpreso dal fuoco: cerca una via di fuga sicura (zone senza vegetazione, corsi d'acqua), non andare controvento, sdraiati a terra se c'è fumo, respira con panno umido.",
            "**COSA FARE DOPO:**\n* Segui indicazioni delle autorità.\n* Bonifica l'area intorno a casa.",
        ],
        "Ordigni Bellici Inesplosi": [ # L.4 pag. 160 -> Pieghevole pag. 161
            "**COSA FARE:**\n* Non toccare l'oggetto.\n* Non rimuovere terra o altri oggetti vicini.\n* Non accendere fuochi.\n* Non usare apparecchi radio-trasmittenti.\n* Segnala il ritrovamento (112, 113, 115).\n* Allontanati e impedisci ad altri di avvicinarsi.\n* Se evacuato: segui le istruzioni, chiudi gas/luce/acqua, porta documenti/medicinali/kit emergenza, raggiungi aree accoglienza.\n* Non rientrare fino a cessato allarme.",
        ],
         "Inquinamento Costiero": [ # M.10 pag. 179 (Norme specifiche non dettagliate come pieghevole nel PEC)
            "**NORME GENERALI:**\n* In caso di avvistamento di inquinamento (sostanze oleose, rifiuti anomali, morie di pesci), segnalare immediatamente alla Capitaneria di Porto (1530) o alle Autorità Locali (Polizia Locale, Comune).\n* Non toccare né tentare di rimuovere autonomamente sostanze sospette spiaggiate o galleggianti.\n* Rispettare scrupolosamente eventuali ordinanze di divieto di balneazione, pesca, o accesso alle spiagge emanate dal Sindaco.\n* Seguire le informazioni ufficiali fornite dalle autorità competenti (Comune, Capitaneria, ARPA Marche).\n* Non consumare prodotti ittici provenienti da zone soggette a divieto di pesca.\n* In caso di partecipazione volontaria ad attività di pulizia (solo se coordinati e autorizzati dalle autorità), utilizzare sempre i Dispositivi di Protezione Individuale forniti e seguire le istruzioni operative."
        ],
         "Maremoto": [ # P.6 pag. 187 -> Pieghevole pag. 187-188
            "**COSA FARE PRIMA:**\n* Informati sul piano comunale e sui segnali di allerta.\n* Identifica le aree sicure (elevate) e i percorsi per raggiungerle.\n* Prepara il kit di emergenza.",
            "**COSA FARE DURANTE:**\n* Se senti un forte terremoto vicino alla costa, allontanati subito dalla spiaggia verso zone elevate.\n* Se vedi un improvviso ritiro del mare, allontanati subito verso zone elevate.\n* Se ricevi un'allerta maremoto, abbandona la spiaggia e raggiungi zone elevate.\n* Segui le vie di fuga indicate.\n* Non usare l'auto.\n* Raggiunto un posto sicuro, resta lì finché le autorità non dichiarano cessato allarme.\n* Se sei in mare, ascolta la radio e non avvicinarti alla costa.\n* Se sei in barca, vai al largo.",
            "**COSA FARE DOPO:**\n* Resta nell'area sicura finché le autorità non lo dicono.\n* Verifica le condizioni tue e degli altri.\n* Usa il telefono solo per emergenze.\n* Non bere acqua dal rubinetto.\n* Non mangiare cibo contaminato dall'acqua.\n* Non rientrare in casa se danneggiata, finché non dichiarata agibile."
        ],
        "Incidente Rilevante Goldengas": [],
        "Manifestazioni ed Eventi Programmati": [
             "**NORME GENERALI PER IL PUBBLICO:**\n* Prendere visione delle planimetrie dell'area con indicazione delle uscite di sicurezza e dei punti di raccolta.\n* Individuare le uscite di sicurezza più vicine alla propria postazione.\n* Seguire le indicazioni del personale di sicurezza (steward) e degli addetti all'emergenza.\n* Mantenere libere le vie di esodo e le uscite di sicurezza.\n* Non introdurre oggetti pericolosi (es. bottiglie di vetro, materiale infiammabile).\n* In caso di emergenza: mantenere la calma, seguire le istruzioni diffuse tramite altoparlanti o dal personale, dirigersi ordinatamente verso l'uscita di sicurezza più vicina, raggiungere il punto di raccolta esterno indicato.\n* Non usare fiamme libere.\n* Segnalare immediatamente al personale di sicurezza eventuali situazioni di pericolo o persone in difficoltà."
         ]
    }
}
# --- Fine Struttura Dati ---

# --- Funzioni Helper per Stato ---
def get_task_key(risk, phase, actor, index):
    """Genera una chiave unica per un'attività nello stato sessione."""
    # Sostituisci spazi e caratteri speciali per creare una chiave valida
    safe_risk = str(risk).replace(" ", "_").replace("-", "_").replace("(", "").replace(")", "")
    safe_phase = str(phase).replace(" ", "_").replace("-", "_").replace("(", "").replace(")", "")
    safe_actor = str(actor).replace(" ", "_").replace("-", "_").replace("/", "_")
    return f"task_{safe_risk}_{safe_phase}_{safe_actor}_{index}"

def initialize_session_state():
    """Inizializza lo stato della sessione se non esiste."""
    if 'task_states' not in st.session_state:
        st.session_state.task_states = {}
    if 'current_risk' not in st.session_state:
        st.session_state.current_risk = None
    if 'current_phase' not in st.session_state:
        st.session_state.current_phase = None

def reset_task_states_if_context_changed(risk, phase):
    """Resetta lo stato delle attività se il rischio o la fase cambiano."""
    if st.session_state.current_risk != risk or st.session_state.current_phase != phase:
        st.session_state.task_states = {}
        st.session_state.current_risk = risk
        st.session_state.current_phase = phase
        # st.experimental_rerun() # Forzare rerun può aiutare a volte ma usare con cautela

# --- Applicazione Streamlit ---
initialize_session_state()

# Configurazione Pagina
st.set_page_config(
    page_title="Gestione Emergenze Interattiva - PEC Senigallia",
    page_icon="📝",
    layout="wide"
)

# --- Sidebar ---
try:
    st.sidebar.image("assets/logo_comune.png", width=150)
except Exception as e:
    st.sidebar.caption("Logo Comune Senigallia (non caricato)")

st.sidebar.title("Navigazione PEC")

rischi_operativi = [
    "Idrogeologico - Idraulico", "Sismico", "Neve",
    "Incendi Boschivi e d’Interfaccia", "Ordigni Bellici Inesplosi",
    "Inquinamento Costiero", "Manifestazioni ed Eventi Programmati", "Maremoto"
]
lista_rischi_validi = [r for r in pec_data.keys() if r in rischi_operativi]

selected_risk = st.sidebar.selectbox(
    "Seleziona Scenario di Rischio Attivo:",
    options=lista_rischi_validi,
    key='risk_selector',
    index=lista_rischi_validi.index(st.session_state.current_risk) if st.session_state.current_risk in lista_rischi_validi else 0
)

selected_phase = None
if selected_risk and selected_risk in pec_data and isinstance(pec_data[selected_risk], dict):
    phases_for_risk = list(pec_data[selected_risk].keys())
    if phases_for_risk:
        # Trova l'indice della fase corrente se esiste, altrimenti default a 0
        current_phase_index = 0
        if st.session_state.current_phase in phases_for_risk and st.session_state.current_risk == selected_risk:
             try:
                 current_phase_index = phases_for_risk.index(st.session_state.current_phase)
             except ValueError:
                 current_phase_index = 0 # Fallback se la fase non è trovata (dovrebbe essere già resettata)

        selected_phase = st.sidebar.selectbox(
            "Seleziona Fase Operativa Corrente:",
            options=phases_for_risk,
            key='phase_selector',
            index=current_phase_index
        )
    else:
        st.sidebar.warning(f"Nessuna fase operativa definita nel PEC per '{selected_risk}'.")
elif selected_risk:
     st.sidebar.error(f"Struttura dati non valida per il rischio '{selected_risk}'.")
else:
    st.sidebar.error("Errore nel caricamento delle fasi.")

# --- Reset Stato Task se Contesto Cambiato ---
# Questo va fatto *dopo* aver letto i valori dai selettori
reset_task_states_if_context_changed(selected_risk, selected_phase)


# (Accesso Rapido Sidebar - omesso per brevità, uguale a prima)
st.sidebar.divider()
st.sidebar.subheader("Accesso Rapido")
# ... (Incolla qui gli expander per Glossario, Acronimi, Funzioni, Aree, Norme)...
with st.sidebar.expander("Glossario"):
    # ... codice glossario ...
    pass
with st.sidebar.expander("Acronimi / Sigle"):
    # ... codice acronimi ...
    pass
with st.sidebar.expander("Funzioni di Supporto (F1-F12)"):
     # ... codice funzioni ...
     pass
with st.sidebar.expander("Aree e Punti di Emergenza"):
     # ... codice aree ...
     pass
with st.sidebar.expander("Norme Comportamento Popolazione"):
     # ... codice norme ...
     pass

# --- Area Principale Interattiva ---

if selected_risk and selected_phase:
    st.header(f"PEC Senigallia: Rischio {selected_risk}")
    st.subheader(f"Fase Operativa: {selected_phase}")
    st.divider()

    stato_opzioni = ["Da Fare", "In Corso", "Completato"]
    stato_icone = {"Da Fare": "⚪", "In Corso": "🟡", "Completato": "✅"}

    # Recupera le azioni per la fase selezionata
    if (selected_risk in pec_data and
        isinstance(pec_data[selected_risk], dict) and
        selected_phase in pec_data[selected_risk] and
        isinstance(pec_data[selected_risk][selected_phase], dict)):

        actions_data = pec_data[selected_risk][selected_phase]

        actors_order = ["Sindaco"] + [f"Funzione {i}" for i in range(1, 13)] # Ordine desiderato
        # Aggiungere eventuali sezioni speciali se necessario e definite in actions_data

        for actor_key in actors_order:
            actor_actions = []
            actor_name = actor_key # Default

            if actor_key == "Sindaco":
                actor_actions = actions_data.get("Sindaco", [])
                actor_name = "Autorità Comunale / Sindaco"
            elif actor_key.startswith("Funzione"):
                 func_num_str = actor_key.split(" ")[1]
                 # Cerca azioni sia come "Funzione X" sia come "FX"
                 actor_actions = actions_data.get(actor_key, [])
                 if not actor_actions:
                     actor_actions = actions_data.get(f"F{func_num_str}", [])

                 # Recupera nome completo della funzione
                 if "FunzioniSupporto" in pec_data and isinstance(pec_data["FunzioniSupporto"], dict):
                      func_data = pec_data["FunzioniSupporto"].get(f"F{func_num_str}", {})
                      if isinstance(func_data, dict):
                          actor_name = f"F{func_num_str} - {func_data.get('Nome', actor_key)}"
                      else:
                          actor_name = actor_key
                 else:
                      actor_name = actor_key

            if not isinstance(actor_actions, list): actor_actions = [] # Assicura sia una lista

            if actor_actions: # Mostra l'expander solo se ci sono azioni
                with st.expander(f"**{actor_name}**", expanded=True): # Espanso di default
                    for i, action_text in enumerate(actor_actions):
                        task_unique_key = get_task_key(selected_risk, selected_phase, actor_key, i)

                        # Inizializza lo stato per questa task se non esiste
                        if task_unique_key not in st.session_state.task_states:
                            st.session_state.task_states[task_unique_key] = {
                                'status': stato_opzioni[0], # Default a "Da Fare"
                                'notes': []
                            }

                        current_status = st.session_state.task_states[task_unique_key]['status']
                        current_notes = st.session_state.task_states[task_unique_key]['notes']

                        col1, col2 = st.columns([3, 1]) # Colonna azione più larga

                        with col1:
                             icon = stato_icone.get(current_status, "❓")
                             st.markdown(f"{icon} {action_text}")

                             # Sezione Note
                             with st.expander("Mostra/Aggiungi Note", expanded=False):
                                 # Mostra note esistenti
                                 if current_notes:
                                     st.write("**Note Precedenti:**")
                                     # Mostra in ordine inverso (più recenti prima)
                                     for ts, note in reversed(current_notes):
                                         st.caption(f"_{ts.strftime('%Y-%m-%d %H:%M:%S')}_")
                                         st.markdown(f"- {note}")
                                     st.divider()
                                 else:
                                      st.caption("Nessuna nota presente.")

                                 # Aggiungi nuova nota
                                 new_note_key = f"new_note_{task_unique_key}"
                                 button_key = f"add_note_btn_{task_unique_key}"
                                 new_note_text = st.text_area("Aggiungi Nota:", key=new_note_key, height=75)
                                 if st.button("Salva Nota", key=button_key):
                                     if new_note_text:
                                         timestamp = datetime.datetime.now()
                                         st.session_state.task_states[task_unique_key]['notes'].append((timestamp, new_note_text))
                                         # Pulisce l'area testo dopo il salvataggio (richiede rerun)
                                         st.session_state[new_note_key] = ""
                                         st.experimental_rerun() # Rerun per aggiornare visualizzazione note e pulire area
                                     else:
                                         st.warning("Inserisci del testo per la nota.")

                        with col2:
                            # Selettore di Stato - Usa radio per chiarezza
                            stato_widget_key = f"status_radio_{task_unique_key}"
                            selected_status = st.radio(
                                "Stato:",
                                options=stato_opzioni,
                                index=stato_opzioni.index(current_status),
                                key=stato_widget_key,
                                horizontal=True, # Layout orizzontale
                                label_visibility="collapsed" # Nasconde label "Stato:"
                            )
                            # Aggiorna lo stato nella sessione se l'utente ha cambiato valore
                            if selected_status != current_status:
                                st.session_state.task_states[task_unique_key]['status'] = selected_status
                                st.experimental_rerun() # Rerun per aggiornare icona e stato effettivo

                        st.divider() # Separatore tra le attività

            # elif actor_key != "Sindaco": # Non mostrare expander vuoti per le funzioni
            #     # Potresti aggiungere un messaggio opzionale qui se vuoi indicare funzioni senza azioni
            #     # st.info(f"Nessuna azione specifica definita nel PEC per {actor_name} in questa fase.")
            #     pass


        # Gestione Sezioni Speciali (se presenti e non già coperte dalle funzioni)
        special_sections = [k for k in actions_data.keys() if k not in actors_order]
        if special_sections:
            st.divider()
            st.subheader("Azioni Specifiche Addizionali / Dettagli")
            for section_name in special_sections:
                 section_actions = actions_data.get(section_name, [])
                 if isinstance(section_actions, list) and section_actions:
                      with st.expander(f"**{section_name}**", expanded=True):
                           for k, action_text in enumerate(section_actions):
                               task_unique_key = get_task_key(selected_risk, selected_phase, section_name, k)
                               # ... (Logica duplicata per stato e note come sopra) ...
                               if task_unique_key not in st.session_state.task_states:
                                    st.session_state.task_states[task_unique_key] = {'status': stato_opzioni[0], 'notes': []}
                                current_status = st.session_state.task_states[task_unique_key]['status']
                                current_notes = st.session_state.task_states[task_unique_key]['notes']

                                col1, col2 = st.columns([3, 1])
                                with col1:
                                     icon = stato_icone.get(current_status, "❓")
                                     st.markdown(f"{icon} {action_text}")
                                     with st.expander("Mostra/Aggiungi Note", expanded=False):
                                          # ... (codice note come sopra) ...
                                          pass # Placeholder
                                with col2:
                                     stato_widget_key = f"status_radio_{task_unique_key}"
                                     selected_status = st.radio(
                                          "Stato:", options=stato_opzioni, index=stato_opzioni.index(current_status),
                                          key=stato_widget_key, horizontal=True, label_visibility="collapsed"
                                     )
                                     if selected_status != current_status:
                                         st.session_state.task_states[task_unique_key]['status'] = selected_status
                                         st.experimental_rerun()
                                st.divider()
                 else:
                      st.info(f"Nessuna azione specifica definita per '{section_name}'.")


    else:
        st.warning(f"Dati non disponibili o in formato non valido per Rischio '{selected_risk}' e Fase '{selected_phase}'.")

# ... (Resto del codice come prima, gestione errori e footer) ...
elif not selected_risk:
    st.info("Seleziona uno scenario di rischio dalla sidebar per iniziare.")
# ... altri casi ...

st.divider()
st.caption("Applicazione Interattiva Supporto Sala Operativa - PEC Comune di Senigallia")
