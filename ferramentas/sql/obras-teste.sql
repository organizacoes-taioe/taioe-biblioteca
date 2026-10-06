-- Catálogo de teste para o workflow Catálogo do taioe-infra (etapa 2/3).
-- O gerador de verdade (etapa 4) grava a lista inteira de obras neste formato.
insert into biblioteca.obras (obra, titulo) values
  ('machado-de-assis/dom-casmurro', 'Dom Casmurro')
on conflict (obra) do update set titulo = excluded.titulo, atualizado_em = now();
