% rebase('base.tpl')

% import model

<div class="container">
  <div class="row">
    <div class="col">

    <div class="p-3">
    <table>
        <tr>
        % for črka in ' abcdefgh':
            <td style='text-align: center'> {{črka}} </td>
        % end
        </tr>
        % vrstica = 8
        <tr>
            <td>
                {{vrstica}}
            </td>
            % for stolpec in range(1, 9):
            <td>
                % polje = str((vrstica + stolpec) % 2)
                % barva_in_figura = igra.postavitev.get((vrstica, stolpec))
                % ime_slike = polje if (vrstica, stolpec) not in igra.postavitev else polje + barva_in_figura[0] + barva_in_figura[1]
                <img src="/sah_img/{{ime_slike}}.jpg" / width="50" height="50" >
            % end
            </td>
        </tr>
        % vrstica = 7
        <tr>
            <td>
                {{vrstica}}
            </td>
            % for stolpec in range(1, 9):
            <td>
                % polje = str((vrstica + stolpec) % 2)
                % barva_in_figura = igra.postavitev.get((vrstica, stolpec))
                % ime_slike = polje if (vrstica, stolpec) not in igra.postavitev else polje + barva_in_figura[0] + barva_in_figura[1]
                <img src="/sah_img/{{ime_slike}}.jpg" / width="50" height="50" >
            % end
            </td>
        </tr>
        % vrstica = 6
        <tr>
            <td>
                {{vrstica}}
            </td>
            % for stolpec in range(1, 9):
            <td>
                % polje = str((vrstica + stolpec) % 2)
                % barva_in_figura = igra.postavitev.get((vrstica, stolpec))
                % ime_slike = polje if (vrstica, stolpec) not in igra.postavitev else polje + barva_in_figura[0] + barva_in_figura[1]
                <img src="/sah_img/{{ime_slike}}.jpg" / width="50" height="50" >
            % end
            </td>
        </tr>
        % vrstica = 5
        <tr>
            <td>
                {{vrstica}}
            </td>
            % for stolpec in range(1, 9):
            <td>
                % polje = str((vrstica + stolpec) % 2)
                % barva_in_figura = igra.postavitev.get((vrstica, stolpec))
                % ime_slike = polje if (vrstica, stolpec) not in igra.postavitev else polje + barva_in_figura[0] + barva_in_figura[1]
                <img src="/sah_img/{{ime_slike}}.jpg" / width="50" height="50" >
            % end
            </td>
        </tr>
        % vrstica = 4
        <tr>
            <td>
                {{vrstica}}
            </td>
            % for stolpec in range(1, 9):
            <td>
                % polje = str((vrstica + stolpec) % 2)
                % barva_in_figura = igra.postavitev.get((vrstica, stolpec))
                % ime_slike = polje if (vrstica, stolpec) not in igra.postavitev else polje + barva_in_figura[0] + barva_in_figura[1]
                <img src="/sah_img/{{ime_slike}}.jpg" / width="50" height="50" >
            % end
            </td>
        </tr>
        % vrstica = 3
        <tr>
            <td>
                {{vrstica}}
            </td>
            % for stolpec in range(1, 9):
            <td>
                % polje = str((vrstica + stolpec) % 2)
                % barva_in_figura = igra.postavitev.get((vrstica, stolpec))
                % ime_slike = polje if (vrstica, stolpec) not in igra.postavitev else polje + barva_in_figura[0] + barva_in_figura[1]
                <img src="/sah_img/{{ime_slike}}.jpg" / width="50" height="50" >
            % end
            </td>
        </tr>
        % vrstica = 2
        <tr>
            <td>
                {{vrstica}}
            </td>
            % for stolpec in range(1, 9):
            <td>
                % polje = str((vrstica + stolpec) % 2)
                % barva_in_figura = igra.postavitev.get((vrstica, stolpec))
                % ime_slike = polje if (vrstica, stolpec) not in igra.postavitev else polje + barva_in_figura[0] + barva_in_figura[1]
                <img src="/sah_img/{{ime_slike}}.jpg" / width="50" height="50" >
            % end
            </td>
        </tr>
        % vrstica = 1
        <tr>
            <td>
                {{vrstica}}
            </td>
            % for stolpec in range(1, 9):
            <td>
                % polje = str((vrstica + stolpec) % 2)
                % barva_in_figura = igra.postavitev.get((vrstica, stolpec))
                % ime_slike = polje if (vrstica, stolpec) not in igra.postavitev else polje + barva_in_figura[0] + barva_in_figura[1]
                <img src="/sah_img/{{ime_slike}}.jpg" / width="50" height="50" >
            % end
            </td>
        </tr>
    </table>
    </div>

    </div>
    <div class="col align-self-center">

    % if stanje == model.ZMAGA:
        <b>Čestitke, zmagali ste!</b>
        <form action="/" method="get">
            <button type="submit">Nova igra</button>
        </form>
    % elif stanje == model.PORAZ:
        <b>Žal ste izgubili. Več sreče prihodnjič!</b>
        <form action="/" method="get">
            <button type="submit">Nova igra</button>
        </form>

    % else:
    <div class="mb-5">
    <form action="/poteza/" method="post">
      Izberite polje, iz katerega želite premakniti figuro: <input type=text name="staro polje" placeholder="1, b" class="form-control">
      <br/>
      Izberite polje, na katerega želite premakniti figuro: <input type=text name="novo polje" placeholder="3, c" class="form-control">
      <br/>
      <div class="mt-2">
      <button type="submit" class="btn btn-outline-dark">Igraj</button>
      </div>
    </form>
    </div>
    % end

    <form action="/" method="get">
      <button type="submit" class="btn btn-outline-dark btn-sm">Izhod</button>
    </form>

    </div>
  </div>
</div>