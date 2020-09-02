% rebase('base.tpl')

<div class="p-5">

<div class="pb-3"> <h1 class="text-center">UVP projekt Šah</h1> </div>

<div class="mb-n3">
<p style="font-size:18px;" class="text-center"> Pozdravljeni! </p>
</div>
<p class="text-center"> Sem študent prvega letnika matematike na FMF in za projektno nalogo pri UVP sem pripravil program za igro šaha. </p>

<form action="/nova_igra/" method="post" class="text-center">

  <p>Izberite težavnost: <select name="tezavnost" size="1" class="btn btn-outline-dark btn-sm dropdown-toggle">
  <option value=1>Lahko</option>
  <option value=2>Srednje</option>
  <option value=3>Težko</option>
  </select></p>

  <p>Izberite barvo: <select name="barva" size="1" class="btn btn-outline-dark btn-sm dropdown-toggle">
  <option value='b'>Bela</option>
  <option value='č'>Črna</option>
  </select></p>

  <button type="submit" class="btn btn-outline-dark">Nova igra</button>

</form>

</div>