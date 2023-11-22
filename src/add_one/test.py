"""
        questa è la descrizione del modulo
        
        Todo:
            * incrementare la documentazione
    
"""
    
def test(numero:int=0,lunghezza:int=3)->str:
    """Trasforma un intero in stringa con lo zeropadding
    
        Args:
            numero: valore da trasformare
            lunghezza: lunghezza della stringa
            
        Returns:
            stinga di lunghezza 3 con il padding

    """
    
    return f"{numero:0{lunghezza}}"


def test2(elem:int,flag:bool=False)->str:
    """
    _summary_

    Args:
        elem (int): _description_
        flag (bool, optional): _description_. Defaults to False.

    Returns:
        str: _description_
    """
    return f"{self.var:0{len}}"
    
class Prova:
    """
    _summary_
    """
    
    def __init__(self,a):
        """
        _summary_

        Args:
            a (_type_): _description_
        """
        self.var=a
        
    def test(self,len:int)->str:
        """
        _summary_

        Args:
            len (int): _description_

        Returns:
            str: _description_
        """
        
        return f"{self.var:0{len}}"
