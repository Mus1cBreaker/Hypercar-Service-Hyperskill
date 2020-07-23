from django.views import View
from django.http.response import HttpResponse, Http404
from django.shortcuts import render, redirect
from tickets.models import CarProblems


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 'tickets/welcome.html'
        )


class MenuView(View):
    def post(self, request, *args, **kwargs):
        _inst.get_card(str(request.POST.get('name')))
        return redirect("/menu/" + str(request.POST.get('name')))

    def get(self, request, *args, **kwargs):
        return render(
            request, 'tickets/menu.html'
        )


class ProblemView(View):
    def get(self, request, problem, *args, **kwargs):
        number = _inst.get_card(problem)
        context = {
            "title": problem,
            "number": _inst.get_last_added(problem),
            "time": _inst.get_time(_inst.get_last_added(problem))
        }
        if not context:
            raise Http404
        return render(
            request, 'tickets/problem.html', context=context
        )


class ProcessingView(View):
    def get(self, request, *args, **kwargs):
        context = {
            "oil_queue": _inst.get_oil_length(),
            "tires_queue": _inst.get_tires_length(),
            "diagnostic_queue": _inst.get_diagnostic_length()
        }
        return render(
            request, 'tickets/processing.html', context=context
        )

    def post(self, request, *args, **kwargs):
        _inst.process_next()
        return redirect("/processing")


class NextView(View):
    def get(self, request, *args, **kwargs):
        context = {
            "next": _inst.last
        }
        return render(
            request, 'tickets/next.html', context=context
        )


_inst = CarProblems()

# Test1 = ProblemView()
# Test1.get("200", "inflate_tires")
# Test1.get("200", "change_oil")
# Test1.get("200", "change_oil")
# Test1.get("200", "inflate_tires")