const BOTAOINICIO = document.getElementById("inicio");
        const BOTAOPARAVOCE = document.getElementById("paravoce");
        const BOTAOSALVOS = document.getElementById("salvos");
        const POPUP_SOLICITA_LOGIN = document.getElementById("solicita_login");
        const POPUP_SOLICITA_ASSINATURA = document.getElementById("solicita_assinatura");
        const POPUPLOGIN = document.getElementById("janela1");
        const POPUPCADASTRO = document.getElementById("janela2");
        const EMAILCADASTRO = document.getElementById("emailcadastro");
        const NOMECADASTRO = document.getElementById("nomecadastro");
        const SENHACADASTRO = document.getElementById("senhacadastro");
        const NOTICIA = document.getElementById("noticia");
        const LOADINGBAR = document.getElementById("loadingScreen");
        const MAINBODY = document.getElementById("mainbody");
        const CONTAINER = document.getElementById("container1");
        const NOTICIA_1 = document.getElementById("noticia_1");
        const NOTICIA_2 = document.getElementById("noticia_2");
        const NOTICIA_3 = document.getElementById("noticia_3");
        const NOTICIA_4 = document.getElementById("noticia_4");
        const NOTICIA_5 = document.getElementById("noticia_5");
        const NOTICIA_6 = document.getElementById("noticia_6");
        const NOTICIA_7 = document.getElementById("noticia_7");
        const NOTICIA_8 = document.getElementById("noticia_8");
        const NOTICIA_9 = document.getElementById("noticia_9");
        


        var inicio = true;
        var paravoce = false;
        var salvos = false;
        var clicou = false;
        var logou = false;

        /*function colocaNoticia(quantidade){
            for(let i=0; i<quantidade; i++){
                var noticia = document.createElement('div');
                noticia.id = "noticias_"+i;
                noticia.classList.add("noticia");

                var principal = document.createElement('div');
                principal.id = "principal_"+i;
                principal.classList.add("principal");
                principal.addEventListener("click", function(event){expande(event.target)});

                var imagem = document.createElement('img');
                imagem.id = "imagem_"+i;
                imagem.src = "Captura de tela 2023-05-01 215707.png";

                var conteudo = document.createElement('div');
                conteudo.classList.add("conteudo");
                conteudo.id = "conteudo_"+i;

                var icone = document.createElement('img');
                icone.classList.add("icone");
                icone.src = "image1.png";

                CONTAINER.appendChild(noticia);
                noticia.appendChild(principal);
                principal.appendChild(imagem);
                principal.appendChild(conteudo);
                conteudo.appendChild(icone);
                conteudo.innerHTML = "<h3>Homem vira cão no interior da paraíba</h3>Conteúdo da publicação Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vel libero vestibulum, tristique tortor vel, eleifend metus. In auctor, libero ut faucibus lobortis, metus mauris tempus ipsum, a tempus ex dolor sed libero. Integer at ex ac sapien fermentum ultrices nec sit amet tortor. Nam euismod purus quis lectus consequat vestibulum. Sed dapibus euismod augue, at eleifend nisl consequat nec. Cras placerat lacus libero, id tempor odio tristique id. Nulla facilisi. Integer pharetra massa nec metus facilisis dignissim. Morbi interdum elit sed odio ultricies, at placerat libero scelerisque. Fusce commodo ultricies lorem, et fringilla orci. Nunc ac mi id enim suscipit semper. Suspendisse eu nunc ut libero congue lacinia. Phasellus vestibulum nulla id vestibulum efficitur. Sed vestibulum nisl magna, non ultricies mauris feugiat in. Vivamus rutrum metus quis varius fringilla. Sed ultricies justo at ligula vehicula, id tempor elit condimentum. Donec ullamcorper vehicula purus, in pulvinar neque scelerisque at. Sed suscipit sem in arcu consectetur, sit amet rhoncus purus fringilla. Maecenas et ligula efficitur, ullamcorper nisi et, dapibus nisi. Cras at sapien quis velit consequat molestie. Morbi eu ex ut urna tempor rutrum eu nec dui. Integer sodales velit ac ultrices ultricies. Cras nec eros mi. Vivamus vitae mauris eu felis dignissim pulvinar. Vivamus in risus ac sapien convallis feugiat ac vel dui. Cras luctus, neque et ultricies convallis, eros dolor finibus risus, vel convallis elit elit et elit. Sed interdum tincidunt est, in auctor est molestie nec. Mauris accumsan rutrum turpis, sed efficitur ex gravida sit amet. Nam luctus, quam eget laoreet ultricies, nunc tortor tempus libero, et posuere ipsum risus ac magna. Integer nec lectus vel dolor suscipit auctor. Etiam efficitur, nulla eu luctus mattis, ipsum ex interdum sem, non congue arcu neque et sem. Aliquam erat volutpat. Integer non urna a nibh dictum iaculis."

                var relacionadas = document.createElement('div');
                relacionadas.id = "relacinadas_"+i;
                relacionadas.classList.add("relacinoadas");

                noticia.appendChild(relacionadas);

                var noticia = CONTAINER.children[0];
                
            }
        }*/

        function mensagem(elemento){
            elemento.style.display = "block";
            setTimeout(function(){
                elemento.style.display = "none";
            }, 2000)
        }

        function limpaCadastro(){
            EMAILCADASTRO.value = null;
            NOMECADASTRO.value = null;
            SENHACADASTRO.value = null;
        }

        function clicouBotaoVoltarJanela(elemento){
            escondeElemento(POPUPLOGIN);
            escondeElemento(POPUPCADASTRO);
            escondeElemento(elemento);
        }

        function erroNoCadastro(elementoerrado){
            elementoerrado.value = "inválido";
            elementoerrado.placeholder.color = "red";
            setTimeout( function fn(){elementoerrado.value=null; elementoerrado.placeholder.color=black;}, 200)
        }

        function clicouBotaoEntrar(){
            //verifica se a conta existe
            //se existe ->
            //pega o nome da conta pelo email e atribui à nomedaconta
            //atualiza a página
            logou = true;
            escondeElemento(POPUPLOGIN);
        }

        function clicouBotaoCadastrar(){
            //verifica se os elementos estão válidos
            //verifica se existe a conta
            //se não existe cria 
            //emailcadastro.value tem o email informado
            //nomecadastro.value tem o nome informado
            //senhacadastro.value tem a senha informada
            escondeElemento(POPUPCADASTRO);
            limpaCadastro();
            //erroNoCadastro(EMAILCADASTRO);  mostra que deu inválido no input


        }

        function clicouBotaoLogin(){
            mostraElemento(POPUPLOGIN);
        }

        function clicouBotaoCadastro(){
            mostraElemento(POPUPCADASTRO);
        }

        function escondeElemento(elemento){
            elemento.style.display="none";
        }

        function mostraElemento(elemento){
            elemento.style.display="flex";
        }

        function pintaBorda(elemento){
            elemento.style.borderColor = "rgb(0, 106, 255)";
            elemento.style.color = "rgb(0, 106, 255)";
        }

        function tiraCor(elemento){
            elemento.style.borderColor = "transparent";
            elemento.style.color = "rgb(255, 255, 255, 0.6)";
        }

        function clicouBotaoSalvos(){
            if(logou==true){
                pintaBorda(BOTAOSALVOS);
                tiraCor(BOTAOINICIO);
                tiraCor(BOTAOPARAVOCE);
                salvos = true;
                inicio = false;
                paravoce = false;
            }else{
                mensagem(POPUP_SOLICITA_ASSINATURA);
            }
        }

        function clicouBotaoParaVoce(){
            //verificar se está logado
            if(logou==true){
                pintaBorda(BOTAOPARAVOCE);
                tiraCor(BOTAOINICIO);
                tiraCor(BOTAOSALVOS);
                inicio = false;
                salvos = false;
                paravoce = true;
            }else{
                mensagem(POPUP_SOLICITA_LOGIN);
            }
            
            //refresh com o conteúdo dedicado
        }

        function clicouBotaoInicio(){
            pintaBorda(BOTAOINICIO);
            tiraCor(BOTAOPARAVOCE);
            tiraCor(BOTAOSALVOS);
            inicio = true;
            paravoce = false;
            salvos = false;
            //refesh com o conteúdo genérico
        }

        function expande(elemento){
            if (clicou == false){
            
                var janela = document.createElement('div');
                janela.classList.add("popUp-background");
                janela.id = "temporario";
                janela.style.display = "flex";
                document.body.appendChild(janela);
                
                var noticia = elemento.cloneNode(true);
                
                noticia.classList.add("noticiaJanela");
                noticia.classList.add("conteudorelacionado");
                janela.appendChild(noticia);
                
                var salvar = document.createElement('div');
                salvar.classList.add("botaoconta");
                salvar.id = "salvar";
                salvar.innerHTML = "Salvar";
                salvar.addEventListener("click", function(){
                    //fazer o registro da notícia 
                    alert("oi");
                })

                var link = document.createElement('button');
                link.classList.add("botaoconta");
                link.id = "salvar";
                link.innerHTML = "Visitar";
                link.addEventListener("click", function(){
                    window.open("https://www.google.com.br", "_blank");
                })

                janela.appendChild(link);
                janela.appendChild(salvar);


                clicou = true;
            }else{
                var janela = window.document.getElementById("temporario");   
                janela.remove();   
                clicou = false;  
            }
        }

        window.addEventListener("load", function(){
            escondeElemento(LOADINGBAR);
            mostraElemento(MAINBODY);
        })

        pintaBorda(BOTAOINICIO);