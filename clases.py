class Tablero:
    def __init__(self,player_id,dim,dict_barcos,tablero_user,tablero_maq):
        self.player_id=player_id
        self.dim=dim
        self.dict_barcos=dict_barcos
        self.tablero_user=tablero_user
        self.tablero_maq=tablero_maq


class display(object):
    """Display HTML representation of multiple objects"""
    template = """<div style="float: left; padding: 10px;">
    <p style='font-family:"Courier New", Courier, monospace'>{0}</p>{1}
    </div>"""
    def __init__(self, *args):
        self.args = args
        
    def _repr_html_(self):
        return '\n'.join(self.template.format(a, eval(a)._repr_html_())
                         for a in self.args)
    
    def __repr__(self):
        return '\n\n'.join(a + '\n' + repr(eval(a))
                           for a in self.args)
        
        
display('df1','df2','pd.concat([df1, df2], axis=1)')
