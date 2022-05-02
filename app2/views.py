from django.views.generic import TemplateView

class Index2View(TemplateView):
    template_name = 'index2.html'

    def get_context_data(self):
        ctxt = super().get_context_data() #superはスーパークラス(親クラス)がに関するオブジェクトを返す関数。ここでの親クラスはDjangoが用意しているTemplateViewなのでそこにある関数を使う
        return ctxt

class About2View(TemplateView):
     template_name = 'about2.html'